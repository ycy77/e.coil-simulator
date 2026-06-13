---
entity_id: "protein.P64512"
entity_type: "protein"
name: "mgrB"
source_database: "UniProt"
source_id: "P64512"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:20041203}; Single-pass membrane protein {ECO:0000305|PubMed:20041203}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mgrB yobG b1826 JW1815"
---

# mgrB

`protein.P64512`

## Static

- Type: `protein`
- Source: `UniProt:P64512`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:20041203}; Single-pass membrane protein {ECO:0000305|PubMed:20041203}.

## Enriched Summary

FUNCTION: Represses PhoP/PhoQ signaling, possibly by binding to the periplasmic domain of PhoQ, altering its activity and that of downstream effector PhoP. PhoP-regulated transcription is redox-sensitive, being activated when the periplasm becomes more reducing (deletion of dsbA/dsbB, treatment with dithiothreitol). MgrB acts between DsbA/DsbB and PhoP/PhoQ in this pathway; the 2 periplasmic Cys residues of MgrB are required for its action on PhoQ, and thus PhoP. {ECO:0000269|PubMed:20041203, ECO:0000269|PubMed:22267510}. MgrB is a small, inner membrane protein that mediates a negative feedback loop in the PhoQP two component system. MgrB negatively regulates the activity of the PHOQ-MONOMER . PhoQ is involved in sensing external magnesium concentrations and then activating PHOP-MONOMER. Thus, by negatively regulating PhoQ activity, MgrB downregulates PhoP activity and the transcription of a wide range of genes whose expression is controlled by PhoP regulation. This set of genes includes mgrB itself . MgrB inhibits the kinase activity of PhoQ; this inhibition drives the partial adaption response that PhoPQ exhibits in response to strong activating stimuli such as a major downward shift in extracellular Mg2+ levels . MgrB localizes to the inner membrane, in accord with prior predictions that it would have a transmembrane segment; MgrB directly interacts with PhoQ...

## Annotation

FUNCTION: Represses PhoP/PhoQ signaling, possibly by binding to the periplasmic domain of PhoQ, altering its activity and that of downstream effector PhoP. PhoP-regulated transcription is redox-sensitive, being activated when the periplasm becomes more reducing (deletion of dsbA/dsbB, treatment with dithiothreitol). MgrB acts between DsbA/DsbB and PhoP/PhoQ in this pathway; the 2 periplasmic Cys residues of MgrB are required for its action on PhoQ, and thus PhoP. {ECO:0000269|PubMed:20041203, ECO:0000269|PubMed:22267510}.

## Outgoing Edges (2)

- `represses` --> [[protein.P23836|protein.P23836]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation
- `represses` --> [[protein.P23837|protein.P23837]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1826|gene.b1826]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64512`
- `KEGG:ecj:JW1815;eco:b1826;ecoc:C3026_10405;`
- `GeneID:93776075;946351;`
- `GO:GO:0005886; GO:0010447; GO:0070298; GO:0071286`

## Notes

PhoP/PhoQ regulator MgrB
