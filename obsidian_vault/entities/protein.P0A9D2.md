---
entity_id: "protein.P0A9D2"
entity_type: "protein"
name: "gstA"
source_database: "UniProt"
source_id: "P0A9D2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gstA gst b1635 JW1627"
---

# gstA

`protein.P0A9D2`

## Static

- Type: `protein`
- Source: `UniProt:P0A9D2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the conjugation of reduced glutathione (GSH) to a wide number of exogenous and endogenous hydrophobic electrophiles. Shows activity toward 1-chloro-2,4-dinitrobenzene (CDNB) and ethacrynic acid. Also possesses thiol:disulfide oxidoreductase activity, using GSH to reduce bis-(2-hydroxyethyl) disulfide (HEDS). Has a low level of glutathione-dependent peroxidase activity toward cumene hydroperoxide. Is important for defense against oxidative stress, probably via its peroxidase activity. {ECO:0000269|PubMed:17018556, ECO:0000269|PubMed:18778244, ECO:0000269|PubMed:2185038, ECO:0000269|PubMed:7798255}. Glutathione S-transferase (Gst) acts as a detoxifying enzyme that is thought to protect the cell from foreign compounds. The enzyme is active toward 1-chloro-2,4-dinitrobenzene . In addition, it also has a low level of glutathione-dependent peroxidase activity toward cumene hydroperoxide as well as thiol:disulfide oxidoreductase activity using bis-(2-hydroxyethyl) disulfide . Crystal structures of Gst have been determined at 2.1 and 1.9 Å resolution . Based on the structural information, Cys10 and His106 are thought to be involved in catalysis . Site-directed mutagenesis of these residues suggest that His106 plays a role in catalysis and Cys10 is involved in binding the glutathione substrate...

## Biological Role

Component of glutathione S-transferase GstA (complex.ecocyc.GST-CPLX).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the conjugation of reduced glutathione (GSH) to a wide number of exogenous and endogenous hydrophobic electrophiles. Shows activity toward 1-chloro-2,4-dinitrobenzene (CDNB) and ethacrynic acid. Also possesses thiol:disulfide oxidoreductase activity, using GSH to reduce bis-(2-hydroxyethyl) disulfide (HEDS). Has a low level of glutathione-dependent peroxidase activity toward cumene hydroperoxide. Is important for defense against oxidative stress, probably via its peroxidase activity. {ECO:0000269|PubMed:17018556, ECO:0000269|PubMed:18778244, ECO:0000269|PubMed:2185038, ECO:0000269|PubMed:7798255}.

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GST-CPLX|complex.ecocyc.GST-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1635|gene.b1635]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9D2`
- `KEGG:ecj:JW1627;eco:b1635;ecoc:C3026_09395;`
- `GeneID:75171696;75204480;945758;`
- `GO:GO:0004364; GO:0005737; GO:0042542; GO:0042803`
- `EC:2.5.1.18`

## Notes

Glutathione S-transferase GstA (EC 2.5.1.18) (GST B1-1)
