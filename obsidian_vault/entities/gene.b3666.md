---
entity_id: "gene.b3666"
entity_type: "gene"
name: "uhpT"
source_database: "NCBI RefSeq"
source_id: "gene-b3666"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3666"
  - "uhpT"
---

# uhpT

`gene.b3666`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3666`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uhpT (gene.b3666) is a gene entity. It encodes uhpT (protein.P0AGC0). Encoded protein function: FUNCTION: Mediates the exchange of external hexose 6-phosphate and internal inorganic phosphate. Can transport glucose-6-phosphate, fructose-6-phosphate and mannose-6-phosphate. Also catalyzes the neutral exchange of internal and external phosphate. {ECO:0000269|PubMed:2197272, ECO:0000269|PubMed:3038843, ECO:0000269|PubMed:3283129, ECO:0000269|PubMed:3522583, ECO:0000269|PubMed:5330662, ECO:0000269|PubMed:8402899}. EcoCyc product frame: UHPT-MONOMER. Genomic coordinates: 3845776-3847167. EcoCyc protein note: UhpT is a hexose phosphate transporter that is a member of the Major Facilitator Superfamily (MFS) . UhpT has been purified and reconstituted into liposomes and demonstrated to transport hexose 6-phosphates via an inorganic phosphate antiport mechanism . The transport system was also shown to catalyze a reversible phosphate: phosphate exchange . Using phosphate-loaded proteoliposomes, and in the absence of any imposed cation motive gradient, hexose 6-phosphate accumulated in the proteoliposomes, and the Km for the transport of 2-deoxy-glucose-6-phosphate via UhpT was determined to be approximately 20 μM . Substrate specificity of UhpT has been studied...

## Biological Role

Activated by crp (protein.P0ACJ8), uvrY (protein.P0AED5), uhpA (protein.P0AGA6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGC0|protein.P0AGC0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=uhpT; function=+
- `activates` <-- [[protein.P0AED5|protein.P0AED5]] `RegulonDB` `S` - regulator=UvrY; target=uhpT; function=+
- `activates` <-- [[protein.P0AGA6|protein.P0AGA6]] `RegulonDB` `C` - regulator=UhpA; target=uhpT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011981,ECOCYC:EG11054,GeneID:948201`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3845776-3847167:-; feature_type=gene
