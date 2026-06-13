---
entity_id: "protein.P39321"
entity_type: "protein"
name: "tamB"
source_database: "UniProt"
source_id: "P39321"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22466966, ECO:0000305|PubMed:25341963}; Single-pass membrane protein {ECO:0000305|PubMed:22466966}; Periplasmic side {ECO:0000269|PubMed:25341963, ECO:0000305|PubMed:22466966, ECO:0000305|PubMed:29129383}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tamB ytfN ytfO b4221 JW4180"
---

# tamB

`protein.P39321`

## Static

- Type: `protein`
- Source: `UniProt:P39321`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22466966, ECO:0000305|PubMed:25341963}; Single-pass membrane protein {ECO:0000305|PubMed:22466966}; Periplasmic side {ECO:0000269|PubMed:25341963, ECO:0000305|PubMed:22466966, ECO:0000305|PubMed:29129383}.

## Enriched Summary

FUNCTION: Component of the translocation and assembly module (TAM), which facilitates the insertion and assembly of specific beta-barrel proteins into the outer membrane (PubMed:22466966, PubMed:25341963, PubMed:29129383, PubMed:39174534). Promotes the assembly and secretion across the outer membrane of a subset of autotransporters, such as Ag43 (PubMed:22466966, PubMed:25341963). Involved in the assembly of the outer membrane usher protein FimD (PubMed:29129383). In vitro, when TAM is reconstituted into preformed liposomes, it can promote the assembly of several outer membrane proteins, including OmpA, EspP, Ag43 and FadL (PubMed:39174534). TamA is sufficient to catalyze a low level of outer membrane protein (OMP) assembly, but both TamA and TamB are required for efficient OMP assembly (PubMed:39174534). TamB may regulate TamA activity (PubMed:25341963). It could regulate conformational changes in TamA to drive its function in OMP assembly (PubMed:26243377). It could also act as a chaperone that facilitate the transport of nascent membrane proteins across the periplasm to TamA in the outer membrane (PubMed:29129383). {ECO:0000269|PubMed:22466966, ECO:0000269|PubMed:25341963, ECO:0000269|PubMed:26243377, ECO:0000269|PubMed:29129383, ECO:0000269|PubMed:39174534}...

## Biological Role

Component of translocation and assembly module (complex.ecocyc.CPLX0-7976).

## Annotation

FUNCTION: Component of the translocation and assembly module (TAM), which facilitates the insertion and assembly of specific beta-barrel proteins into the outer membrane (PubMed:22466966, PubMed:25341963, PubMed:29129383, PubMed:39174534). Promotes the assembly and secretion across the outer membrane of a subset of autotransporters, such as Ag43 (PubMed:22466966, PubMed:25341963). Involved in the assembly of the outer membrane usher protein FimD (PubMed:29129383). In vitro, when TAM is reconstituted into preformed liposomes, it can promote the assembly of several outer membrane proteins, including OmpA, EspP, Ag43 and FadL (PubMed:39174534). TamA is sufficient to catalyze a low level of outer membrane protein (OMP) assembly, but both TamA and TamB are required for efficient OMP assembly (PubMed:39174534). TamB may regulate TamA activity (PubMed:25341963). It could regulate conformational changes in TamA to drive its function in OMP assembly (PubMed:26243377). It could also act as a chaperone that facilitate the transport of nascent membrane proteins across the periplasm to TamA in the outer membrane (PubMed:29129383). {ECO:0000269|PubMed:22466966, ECO:0000269|PubMed:25341963, ECO:0000269|PubMed:26243377, ECO:0000269|PubMed:29129383, ECO:0000269|PubMed:39174534}.; FUNCTION: In addition, is involved in outer membrane lipid homeostasis (PubMed:34781743, PubMed:35226662, PubMed:38913742). Likely transports phospholipids between the inner membrane and the outer membrane (PubMed:34781743, PubMed:35226662, PubMed:38913742). It would provide a bridge-like structure that protects phospholipids as they travel across the periplasm (PubMed:34781743). One possible explanation for the apparent dual function of TAM is that TamB is a somewhat generic transporter of hydrophobic molecules (PubMed:39174534). {ECO:0000269|PubMed:34781743, ECO:0000269|PubMed:35226662, ECO:0000269|PubMed:38913742, ECO:0000269|PubMed:39174534}.; FUNCTION: TamB, YdbH and YhdP are redundant, but not equivalent, in performing an essential function for growth and maintaining lipid homeostasis in the outer membrane (PubMed:34781743). The transport functions of TamB and YhdP could be differentiated according to the fatty acid saturation state of the phospholipids, with TamB transporting more unsaturated phospholipids and YhdP more saturated phospholipids (PubMed:38913742). Any of these three proteins is sufficient for growth (PubMed:34781743). {ECO:0000269|PubMed:34781743, ECO:0000269|PubMed:38913742}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7976|complex.ecocyc.CPLX0-7976]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4221|gene.b4221]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39321`
- `KEGG:ecj:JW4180;eco:b4221;ecoc:C3026_22800;`
- `GeneID:948742;`
- `GO:GO:0005886; GO:0009279; GO:0009306; GO:0089705; GO:0097347`

## Notes

Translocation and assembly module subunit TamB (Autotransporter assembly factor TamB) (Intermembrane phospholipid transporter TamB) (Phospholipid transport protein TamB)
