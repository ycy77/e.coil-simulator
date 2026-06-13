---
entity_id: "gene.b2659"
entity_type: "gene"
name: "glaH"
source_database: "NCBI RefSeq"
source_id: "gene-b2659"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2659"
  - "glaH"
---

# glaH

`gene.b2659`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2659`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glaH (gene.b2659) is a gene entity. It encodes glaH (protein.P76621). Encoded protein function: FUNCTION: Acts as an alpha-ketoglutarate-dependent dioxygenase catalyzing hydroxylation of glutarate (GA) to L-2-hydroxyglutarate (L2HG) in the stationary phase of E.coli. Functions in a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate. Other dicarboxylic acids (oxalate, malonate, succinate, adipate, and pimelate) are not substrates for this enzyme. {ECO:0000269|PubMed:30498244}. EcoCyc product frame: G7394-MONOMER. EcoCyc synonyms: csi-12, ygaT, csiD. Genomic coordinates: 2788985-2789962.

## Biological Role

Repressed by arcA (protein.P0A9Q1), glaR (protein.P37338), nac (protein.Q47005). Activated by lrp (protein.P0ACJ0), crp (protein.P0ACJ8), nac (protein.Q47005).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76621|protein.P76621]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=glaH; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=glaH; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=glaH; function=-+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=glaH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `C` - regulator=GlaR; target=glaH; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=glaH; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008754,ECOCYC:G7394,GeneID:948076`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2788985-2789962:+; feature_type=gene
