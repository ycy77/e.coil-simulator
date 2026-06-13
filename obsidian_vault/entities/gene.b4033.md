---
entity_id: "gene.b4033"
entity_type: "gene"
name: "malF"
source_database: "NCBI RefSeq"
source_id: "gene-b4033"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4033"
  - "malF"
---

# malF

`gene.b4033`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4033`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malF (gene.b4033) is a gene entity. It encodes malF (protein.P02916). Encoded protein function: FUNCTION: Part of the ABC transporter complex MalEFGK involved in maltose/maltodextrin import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:2026607, ECO:0000269|PubMed:2155217}. EcoCyc product frame: MALF-MONOMER. Genomic coordinates: 4243531-4245075. EcoCyc protein note: MalF is an integral membrane component of the maltose ABC transporter . A MalF-MalG heterodimer forms the translocation channel of the maltose ABC transporter; the MalF-MalG channel contacts the MalK dimer at the cytoplasmic face of the membrane and the MalE binding protein at the periplasmic face of the membrane MalF contains 8 transmembrane (TM) helices; in a crystal structure of the maltose transporter in complex with MalE, maltose and ATP, the MalF periplasmic loop (P2) located between TM 3 and 4 is a major area of contact with the maltose binding protein MalE, while an EAA loop located between TM 6 and 7 is a major area of contact with the MalK dimer . malF mutations that alter the substrate specificity of the maltose ABC transporter have been isolated and characterised . Insertion of MalF into the cytoplasmic membrane is SecE- and SecA-dependent ; MalF can assemble in the membrane independently of the bacterial secretion machinery .

## Biological Role

Activated by rpoD (protein.P00579), malT (protein.P06993), fis (protein.P0A6R3), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02916|protein.P02916]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=malF; function=+
- `activates` <-- [[protein.P06993|protein.P06993]] `RegulonDB` `C` - regulator=MalT; target=malF; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=malF; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=malF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013195,ECOCYC:EG10555,GeneID:948532`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4243531-4245075:-; feature_type=gene
