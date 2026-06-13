---
entity_id: "gene.b2199"
entity_type: "gene"
name: "ccmC"
source_database: "NCBI RefSeq"
source_id: "gene-b2199"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2199"
  - "ccmC"
---

# ccmC

`gene.b2199`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2199`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ccmC (gene.b2199) is a gene entity. It encodes ccmC (protein.P0ABM1). Encoded protein function: FUNCTION: Required for the export of heme to the periplasm for the biogenesis of c-type cytochromes. EcoCyc product frame: CCMC-MONOMER. EcoCyc synonyms: yejT, yejU. Genomic coordinates: 2295583-2296320. EcoCyc protein note: CcmC is an inner membrane protein required for for the transfer of heme to the periplasmic heme chaperone CCME-MONOMER CcmE during PWY-8147 "type I cytochrome c biogenesis". ccmC is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmC deletion mutant cannot synthesize holocytochrome c; CcmC is required for covalent incorporation of heme into the periplasmic heme chaperone CCME-MONOMER CcmE . CcmC is predicted to contain six transmembrane helices plus a periplasmic domain that contains the functionally important tryptophan-rich motif (the WWD domain) and two strictly conserved histidines implicated in heme binding (see also )...

## Biological Role

Repressed by narL (protein.P0AF28), narP (protein.P31802). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABM1|protein.P0ABM1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ccmC; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ccmC; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=ccmC; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmC; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ccmC; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmC; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007275,ECOCYC:EG12057,GeneID:946703`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2295583-2296320:-; feature_type=gene
