---
entity_id: "molecule.C00780"
entity_type: "small_molecule"
name: "Serotonin"
source_database: "KEGG"
source_id: "C00780"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Serotonin"
  - "3-(2-Aminoethyl)-1H-indol-5-ol"
  - "5-Hydroxytryptamine"
  - "Enteramine"
---

# Serotonin

`molecule.C00780`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00780`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Serotonin; 3-(2-Aminoethyl)-1H-indol-5-ol; 5-Hydroxytryptamine; Enteramine SEROTONIN "Serotonin" is a monoamine neurotransmitter found in the CNS and gut. It was first discovered in the blood serum as a vasoconstrictor substance . In the CNS, serotonin is causally involved in the regulation of mood, sleep, appetite, memory and learning . Modulation of serotonin at synapses is the modus operandi of several classes of antidepressants. Serotonin in the periphery is expressed in the enterochromaffin cells of the gastrointestinal tract and regulates gut motility. Released from the enterochromaffin cells, it is taken up by platelets and plays a role in primary homeostasis and cell mediated immune responses . Circulating SEROTONIN derived from peripheral tissues is primarily metabolized in the liver to 5-HYDROXYINDOLE_ACETATE, which is excreted in the urine, see PWY-6313.

## Enriched Pathways

- `eco00380` Tryptophan metabolism (KEGG)

## Annotation

KEGG compound: Serotonin; 3-(2-Aminoethyl)-1H-indol-5-ol; 5-Hydroxytryptamine; Enteramine

## Pathways

- `eco00380` Tryptophan metabolism (KEGG)

## Outgoing Edges (1)

- `activates` --> [[reaction.ecocyc.RXN0-5224|reaction.ecocyc.RXN0-5224]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00780`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
