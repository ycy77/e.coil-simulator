---
entity_id: "gene.b3320"
entity_type: "gene"
name: "rplC"
source_database: "NCBI RefSeq"
source_id: "gene-b3320"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3320"
  - "rplC"
---

# rplC

`gene.b3320`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3320`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplC (gene.b3320) is a gene entity. It encodes rplC (protein.P60438). Encoded protein function: FUNCTION: One of two assembly initiator proteins, it binds directly near the 3'-end of the 23S rRNA, where it nucleates assembly of the 50S subunit. {ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:6760192}. EcoCyc product frame: EG10866-MONOMER. Genomic coordinates: 3452297-3452926. EcoCyc protein note: The L3 protein is a component of the 50S subunit of the ribosome. L3 and L24 are the two proteins that initiate assembly of the 50S subunit . The L3 protein is methylated at the glutamine residue in position 150 . A prmB mutant which lacks methylation of L3 has a cold-sensitive growth phenotype and accumulates abnormal ribosomal particles; however, lack of L3 methylation does not appear to affect ribosome function once the ribosome is assembled . L3 interacts with 23S rRNA ; this interaction appears to be cooperative with L6 . An L3 mutant strain is resistant to the antibiotics tiamulin (a peptidyl transferase inhibitor) and pleuromutilin, but not valnemulin . An amber mutation in rplC exerts a polar effect on the genes distal to the rplC gene in the S10 operon .

## Biological Role

Repressed by fliX (gene.b4827). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60438|protein.P60438]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rplC; function=+
- `represses` <-- [[gene.b4827|gene.b4827]] `RegulonDB` `S` - regulator=FliX; target=rplC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010860,ECOCYC:EG10866,GeneID:947817`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3452297-3452926:-; feature_type=gene
