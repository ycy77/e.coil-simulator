---
entity_id: "protein.P33650"
entity_type: "protein"
name: "feoB"
source_database: "UniProt"
source_id: "P33650"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "feoB b3409 JW3372"
---

# feoB

`protein.P33650`

## Static

- Type: `protein`
- Source: `UniProt:P33650`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Transporter of a GTP-driven Fe(2+) uptake system, probably couples GTP-binding to channel opening and Fe(2+) uptake (PubMed:12446835, PubMed:19629046). A guanine nucleotide-binding protein (G proteins) in which the guanine nucleotide binding site alternates between an active, GTP-bound state and an inactive, GDP-bound state. This protein has fast intrinsic GDP release, mediated by the G5 loop (about residues 149-158). Presumably GTP hydrolysis leads to conformational changes and channel closing (PubMed:19629046). A GDP release mechanism involving a conformational change of the G5 loop (and thus the removal of the nucleotide-binding and stabilizing interactions) would significantly reduce the affinity for GDP, and conceivably be sufficient for catalysing nucleotide release (PubMed:25374115). {ECO:0000269|PubMed:12446835, ECO:0000269|PubMed:19629046, ECO:0000269|PubMed:23104801, ECO:0000269|PubMed:25374115, ECO:0000269|PubMed:25517170, ECO:0000269|PubMed:8407793}. FeoB is the inner membrane component of a ferrous iron uptake system which is active under anaerobic growth conditions . FeoB is composed of a hydrophilic N-terminal domain which specifically binds GTP (the G protein domain; residues 1-170), a GDP dissociation inhibitor-like (GDI-like) domain (residues 171-274) and a C-terminal integral membrane domain which may act as a permease...

## Biological Role

Catalyzes G protein coupled Fe2+ transport (reaction.ecocyc.TRANS-RXN-424). Transports GDP (molecule.C00035), GTP (molecule.C00044), Fe2+ (molecule.C14818), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Transporter of a GTP-driven Fe(2+) uptake system, probably couples GTP-binding to channel opening and Fe(2+) uptake (PubMed:12446835, PubMed:19629046). A guanine nucleotide-binding protein (G proteins) in which the guanine nucleotide binding site alternates between an active, GTP-bound state and an inactive, GDP-bound state. This protein has fast intrinsic GDP release, mediated by the G5 loop (about residues 149-158). Presumably GTP hydrolysis leads to conformational changes and channel closing (PubMed:19629046). A GDP release mechanism involving a conformational change of the G5 loop (and thus the removal of the nucleotide-binding and stabilizing interactions) would significantly reduce the affinity for GDP, and conceivably be sufficient for catalysing nucleotide release (PubMed:25374115). {ECO:0000269|PubMed:12446835, ECO:0000269|PubMed:19629046, ECO:0000269|PubMed:23104801, ECO:0000269|PubMed:25374115, ECO:0000269|PubMed:25517170, ECO:0000269|PubMed:8407793}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-424|reaction.ecocyc.TRANS-RXN-424]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3409|gene.b3409]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33650`
- `KEGG:ecj:JW3372;eco:b3409;ecoc:C3026_18495;`
- `GeneID:947919;`
- `GO:GO:0005525; GO:0005886; GO:0006974; GO:0015093; GO:0042802; GO:0098711`

## Notes

Fe(2+) transporter FeoB (Ferrous iron transport protein B)
