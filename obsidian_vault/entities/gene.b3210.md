---
entity_id: "gene.b3210"
entity_type: "gene"
name: "arcB"
source_database: "NCBI RefSeq"
source_id: "gene-b3210"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3210"
  - "arcB"
---

# arcB

`gene.b3210`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3210`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arcB (gene.b3210) is a gene entity. It encodes arcB (protein.P0AEC3). Encoded protein function: FUNCTION: Member of the two-component regulatory system ArcB/ArcA. Sensor-regulator protein for anaerobic repression of the arc modulon. Activates ArcA via a four-step phosphorelay. ArcB can also dephosphorylate ArcA by a reverse phosphorelay involving His-717 and Asp-576. EcoCyc product frame: PHOSPHO-ARCB-HIS. Genomic coordinates: 3350689-3353025. EcoCyc protein note: This is the histidine-717 phosphorylated form of ARCB-MONOMER "ArcB" - the sensor histidine kinase of the ArcAB two-component signal transduction system. EcoCyc protein note: This is the aspartate-576 phosphorylated form of ARCB-CPLX "ArcB" - the sensor histidine kinase of the ArcAB two-component signal transduction system. EcoCyc protein note: This is the histidine-292 phosphorylated form of ARCB-CPLX "ArcB" - the sensor histidine kinase of the ArcAB two-component signal transduction system. EcoCyc protein note: ArcB is the sensor histidine kinase of the ArcAB two-component system which mediates anaerobic repression of numerous enzymes associated with aerobic metabolism...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEC3|protein.P0AEC3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010537,ECOCYC:EG10062,GeneID:947887`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3350689-3353025:-; feature_type=gene
