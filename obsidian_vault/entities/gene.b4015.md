---
entity_id: "gene.b4015"
entity_type: "gene"
name: "aceA"
source_database: "NCBI RefSeq"
source_id: "gene-b4015"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4015"
  - "aceA"
---

# aceA

`gene.b4015`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4015`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aceA (gene.b4015) is a gene entity. It encodes aceA (protein.P0A9G6). Encoded protein function: FUNCTION: Involved in the metabolic adaptation in response to environmental changes. Catalyzes the reversible formation of succinate and glyoxylate from isocitrate, a key step of the glyoxylate cycle, which operates as an anaplerotic route for replenishing the tricarboxylic acid cycle during growth on fatty acid substrates. {ECO:0000269|PubMed:15748982, ECO:0000269|PubMed:3281659, ECO:0000269|PubMed:3291954, ECO:0000269|PubMed:7826335, ECO:0000269|Ref.9}. EcoCyc product frame: ISOCIT-LYASE-MONOMER. EcoCyc synonyms: icl. Genomic coordinates: 4217109-4218413.

## Biological Role

Repressed by iclR (protein.P16528). Activated by rpoD (protein.P00579), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9G6|protein.P0A9G6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aceA; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=aceA; function=+
- `represses` <-- [[protein.P16528|protein.P16528]] `RegulonDB` `S` - regulator=IclR; target=aceA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013128,ECOCYC:EG10022,GeneID:948517`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4217109-4218413:+; feature_type=gene
