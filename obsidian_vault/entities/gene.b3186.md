---
entity_id: "gene.b3186"
entity_type: "gene"
name: "rplU"
source_database: "NCBI RefSeq"
source_id: "gene-b3186"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3186"
  - "rplU"
---

# rplU

`gene.b3186`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3186`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplU (gene.b3186) is a gene entity. It encodes rplU (protein.P0AG48). Encoded protein function: FUNCTION: This protein binds to 23S rRNA in the presence of protein L20. {ECO:0000269|PubMed:2665813, ECO:0000269|PubMed:6170935}. EcoCyc product frame: EG50001-MONOMER. Genomic coordinates: 3333140-3333451. EcoCyc protein note: The L21 protein is a component of the 50S subunit of the ribosome. L21 interacts with 23S rRNA . L4, L5, and L21 bind to erythromycin cooperatively . The rplU gene is expressed from an operon along with rpmA, yhbE, and obgE under control of the rplU promoter. This operon is mainly expressed during exponential growth and is probably indirectly regulated by ppGpp/DksA .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), mlrA (protein.P33358).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG48|protein.P0AG48]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rplU; function=+
- `activates` <-- [[protein.P33358|protein.P33358]] `RegulonDB` `S` - regulator=MlrA; target=rplU; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rplU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010470,ECOCYC:EG50001,GeneID:949057`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3333140-3333451:-; feature_type=gene
