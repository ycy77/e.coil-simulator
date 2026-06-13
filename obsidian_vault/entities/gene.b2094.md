---
entity_id: "gene.b2094"
entity_type: "gene"
name: "gatA"
source_database: "NCBI RefSeq"
source_id: "gene-b2094"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2094"
  - "gatA"
---

# gatA

`gene.b2094`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2094`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gatA (gene.b2094) is a gene entity. It encodes gatA (protein.P69828). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. The enzyme II complex composed of GatA, GatB and GatC is involved in galactitol transport. It can also use D-glucitol. {ECO:0000269|PubMed:1100608, ECO:0000269|PubMed:8955298}. EcoCyc product frame: GATA-MONOMER. Genomic coordinates: 2174597-2175049. EcoCyc protein note: gatA sequenced from a wild-type isolate of E. coli, strain EC3132, encodes a small hydrophilic protein .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), nac (protein.Q47005).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69828|protein.P69828]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gatA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=gatA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=gatA; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=gatA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006932,ECOCYC:EG12414,GeneID:946633`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2174597-2175049:-; feature_type=gene
