---
entity_id: "gene.b4316"
entity_type: "gene"
name: "fimC"
source_database: "NCBI RefSeq"
source_id: "gene-b4316"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4316"
  - "fimC"
---

# fimC

`gene.b4316`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4316`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fimC (gene.b4316) is a gene entity. It encodes fimC (protein.P31697). Encoded protein function: FUNCTION: Required for the biogenesis of type 1 fimbriae. Binds and interact with FimH. EcoCyc product frame: EG10310-MONOMER. EcoCyc synonyms: pilB. Genomic coordinates: 4544304-4545029. EcoCyc protein note: FimC is a member of the periplasmic chaperone family which functions in the chaperone-usher pathway and is indispensable in the biogenesis of the type 1 pilus fiber of Escherichia coli . Type 1 pili mediate recognition of and adhesion to, host tissues and much of our knowledge regarding type 1 pili in E. coli is derived from studies using uropathogenic (UPEC) strains. FimC binds to and forms stable complexes with individual pilus subunits in a process called donor strand complementation (DSC) whereby a polypeptide strand from the N terminal domain of the chaperone is used to complement an 'incomplete' pilus subunit by inserting into an exposed hydrophobic groove . DSC facilitates pilus subunit folding . FimC consists of two immunoglobulin-like domains connected by a short linker peptide . The crystal structure of the FimC-FimH chaperone-adhesin complex from UPEC has been determined to 2.5 A resolution . The FimC sequence shows a high degree of homology to the immunoglobulin-like PapD chaperone from the P-pilus system in uropathogenic E.coli . E...

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3), hns (protein.P0ACF8), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31697|protein.P31697]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fimC; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=fimC; function=+
- `activates` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=fimC; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=fimC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014149,ECOCYC:EG10310,GeneID:948843`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4544304-4545029:+; feature_type=gene
