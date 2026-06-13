---
entity_id: "gene.b4320"
entity_type: "gene"
name: "fimH"
source_database: "NCBI RefSeq"
source_id: "gene-b4320"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4320"
  - "fimH"
---

# fimH

`gene.b4320`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4320`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fimH (gene.b4320) is a gene entity. It encodes fimH (protein.P08191). Encoded protein function: FUNCTION: Involved in regulation of length and mediation of adhesion of type 1 fimbriae (but not necessary for the production of fimbriae). Adhesin responsible for the binding to D-mannose. It is laterally positioned at intervals in the structure of the type 1 fimbriae. In order to integrate FimH in the fimbriae FimF and FimG are needed. {ECO:0000269|PubMed:1971261}. EcoCyc product frame: EG10315-MONOMER. EcoCyc synonyms: pilE. Genomic coordinates: 4548808-4549710. EcoCyc protein note: Type 1, or mannose-sensitive, fimbriae in Escherichia coli mediate binding to receptor structures allowing the bacteria to colonize various host tissues. Receptor recognition is a function of the FimH adhesin of the fimbriae . FimH protein is located both at the tip of the fimbria as well as interspersed along the shaft . Two-dimensional gel electrophoresis suggests that FimH has a molecular weight of 30 kDa and is present in a 1:100 ratio with the major fimbrial subunit, FimA . The binding phenotype of type 1 fimbriae is sensitive to minor amino acid changes in the FimH protein . Mutational studies have identified residues important for the interaction between FimD, an usher involved in fimbriae polymerization, and FimH...

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3), bolA (protein.P0ABE2), hns (protein.P0ACF8), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08191|protein.P08191]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fimH; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=fimH; function=+
- `activates` <-- [[protein.P0ABE2|protein.P0ABE2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=fimH; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=fimH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014157,ECOCYC:EG10315,GeneID:948847`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4548808-4549710:+; feature_type=gene
