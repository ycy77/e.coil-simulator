---
entity_id: "protein.P77348"
entity_type: "protein"
name: "mppA"
source_database: "UniProt"
source_id: "P77348"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:9495761}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mppA ynaH b1329 JW1322"
---

# mppA

`protein.P77348`

## Static

- Type: `protein`
- Source: `UniProt:P77348`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:9495761}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MppA-OppBCDF involved in the uptake of the cell wall murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate (PubMed:9495761). Is involved in the recycling of cell wall peptides (PubMed:9495761). Binds the cell wall peptide L-Ala-D-Gly-gamma-meso-diaminopimelic acid (PubMed:21705338, PubMed:9495761). Can also transport ordinary alpha-linked tripeptides such as Pro-Phe-Lys, but with much lower efficiency than OppA (PubMed:9495761). Cannot bind typical tripeptides such as Lys-Glu-Lys, Lys-Lys-Lys or Ala-Ala-Ala (PubMed:21705338). {ECO:0000269|PubMed:21705338, ECO:0000269|PubMed:9495761}. MppA is the periplasmic binding protein of an ABC transporter that mediates the high affinity uptake of murein tripeptides . mppA mutants cannot use murein tripeptide (L-alanyl-γ-D-glutamyl-meso-diaminopimelate) as a source of diaminopimelic acid (Dap) in a strain that requires Dap for growth . MppA (in the absence of the periplasmic oligopeptide binding protein OppA) supports growth of a proline auxotroph on Pro-Phe-Lys tripeptide; MppA transports murein tripeptide more efficiently than Pro-Phe-Lys...

## Biological Role

Component of murein tripeptide ABC transporter (complex.ecocyc.CPLX0-3970).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex MppA-OppBCDF involved in the uptake of the cell wall murein tripeptide L-alanyl-gamma-D-glutamyl-meso-diaminopimelate (PubMed:9495761). Is involved in the recycling of cell wall peptides (PubMed:9495761). Binds the cell wall peptide L-Ala-D-Gly-gamma-meso-diaminopimelic acid (PubMed:21705338, PubMed:9495761). Can also transport ordinary alpha-linked tripeptides such as Pro-Phe-Lys, but with much lower efficiency than OppA (PubMed:9495761). Cannot bind typical tripeptides such as Lys-Glu-Lys, Lys-Lys-Lys or Ala-Ala-Ala (PubMed:21705338). {ECO:0000269|PubMed:21705338, ECO:0000269|PubMed:9495761}.

## Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3970|complex.ecocyc.CPLX0-3970]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1329|gene.b1329]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77348`
- `KEGG:ecj:JW1322;eco:b1329;ecoc:C3026_07785;`
- `GeneID:75203446;945951;`
- `GO:GO:0015031; GO:0015833; GO:0015834; GO:0016020; GO:0030288; GO:0035351; GO:0042597; GO:0042938; GO:0042939; GO:0055052; GO:0140207; GO:1900750; GO:1904680`

## Notes

Periplasmic murein peptide-binding protein MppA (Murein peptide permease A)
