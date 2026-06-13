---
entity_id: "gene.b0152"
entity_type: "gene"
name: "fhuD"
source_database: "NCBI RefSeq"
source_id: "gene-b0152"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0152"
  - "fhuD"
---

# fhuD

`gene.b0152`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0152`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fhuD (gene.b0152) is a gene entity. It encodes fhuD (protein.P07822). Encoded protein function: FUNCTION: Part of the ABC transporter complex FhuCDB involved in iron(3+)-hydroxamate import. Binds the iron(3+)-hydroxamate complex and transfers it to the membrane-bound permease. Required for the transport of all iron(3+)-hydroxamate siderophores such as ferrichrome, gallichrome, desferrioxamine, coprogen, aerobactin, shizokinen, rhodotorulic acid and the antibiotic albomycin. {ECO:0000269|PubMed:10742172, ECO:0000269|PubMed:11805094, ECO:0000269|PubMed:2254301, ECO:0000269|PubMed:34887516, ECO:0000269|PubMed:8522527}. EcoCyc product frame: FHUD-MONOMER. Genomic coordinates: 170575-171465. EcoCyc protein note: FhuD is the periplasmic siderophore binding component of an iron(III) hydroxamate ABC transporter. Purified FhuD binds ferrichrome (Kd = 1 µM), ferric coprogen (Kd = 0.3 µM), ferric aerobactin (Kd = 0.4 µM) and the antibiotic albomycin (Kd = 5.4 µM). It also binds ferrichrome A, ferrioxamine B and ferrioxamine E with lower affinity (Kd = 79, 36, and 42 µM, respectively) . Peptide mapping experiments suggest that FhuD binds to periplasmic loop 2, cytoplasmic loop 7 and the transmembrane region of FhuB...

## Biological Role

Repressed by fur (protein.P0A9A9).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07822|protein.P07822]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fhuD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000524,ECOCYC:EG10305,GeneID:947510`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:170575-171465:+; feature_type=gene
