---
entity_id: "gene.b3175"
entity_type: "gene"
name: "secG"
source_database: "NCBI RefSeq"
source_id: "gene-b3175"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3175"
  - "secG"
---

# secG

`gene.b3175`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3175`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

secG (gene.b3175) is a gene entity. It encodes secG (protein.P0AG99). Encoded protein function: FUNCTION: Subunit of the protein translocation channel SecYEG. Overexpression of some hybrid proteins has been thought to jam the protein secretion apparatus resulting in cell death; while this may be true it also results in FtsH-mediated degradation of SecY. Treatment with antibiotics that block translation elongation such as chloramphenicol also leads to degradation of SecY and SecE but not SecG. EcoCyc product frame: SECG. EcoCyc synonyms: prlH. Genomic coordinates: 3322173-3322505. EcoCyc protein note: The SecG inner membrane protein is a component of the heterotrimeric SecYEG preprotein translocase. SecY, SecE and an unidentified polypeptide termed 'band1' (later shown to be SecG ) form a stable complex which supports precursor protein translocation in vitro . SecG stimulates translocation of a model secretory protein in SecYE containing proteoliposomes . SecG is not required for SecA binding to SecYE containing proteoliposomes; the translocation ATPase activity of SecA in SecYE containing proteoliposomes is enhanced by the presence of SecG . SecG participates in preprotein signal sequence recognition . SecG contributes to the stability of the translocase and to the interaction with signal sequence...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG99|protein.P0AG99]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=secG; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=secG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010436,ECOCYC:EG12095,GeneID:947720`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3322173-3322505:-; feature_type=gene
