---
entity_id: "reaction.ecocyc.GLUTDEHYD-RXN"
entity_type: "reaction"
name: "GLUTDEHYD-RXN"
source_database: "EcoCyc"
source_id: "GLUTDEHYD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTDEHYD-RXN

`reaction.ecocyc.GLUTDEHYD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTDEHYD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glutamic acid, as the donor of an α-amino group in transaminase reactions, is a key metabolite for the biosynthesis of amino acids. There are two reactions responsible for the biosynthesis of glutamic acid: glutamate synthase and glutamate dehydrogenase Both enzymes provide a route for incorporation of nitrogen into organic compounds, and thus a link between carbohydrate and amino acid metabolism EcoCyc reaction equation: GLT + WATER + NADP -> PROTON + AMMONIUM + 2-KETOGLUTARATE + NADPH; direction=REVERSIBLE. Glutamic acid, as the donor of an α-amino group in transaminase reactions, is a key metabolite for the biosynthesis of amino acids. There are two reactions responsible for the biosynthesis of glutamic acid: glutamate synthase and glutamate dehydrogenase Both enzymes provide a route for incorporation of nitrogen into organic compounds, and thus a link between carbohydrate and amino acid metabolism

## Biological Role

Catalyzed by glutamate dehydrogenase (complex.ecocyc.GDHA-CPLX), glutamate synthase (complex.ecocyc.GLUTAMATESYN-CPLX). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), L-Glutamate (molecule.C00025). Products: NADPH (molecule.C00005), 2-Oxoglutarate (molecule.C00026), H+ (molecule.C00080), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.GLUTSYNIII-PWY` L-glutamate biosynthesis III (EcoCyc)

## Annotation

Glutamic acid, as the donor of an α-amino group in transaminase reactions, is a key metabolite for the biosynthesis of amino acids. There are two reactions responsible for the biosynthesis of glutamic acid: glutamate synthase and glutamate dehydrogenase Both enzymes provide a route for incorporation of nitrogen into organic compounds, and thus a link between carbohydrate and amino acid metabolism

## Pathways

- `ecocyc.GLUTSYNIII-PWY` L-glutamate biosynthesis III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.GDHA-CPLX|complex.ecocyc.GDHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.GLUTAMATESYN-CPLX|complex.ecocyc.GLUTAMATESYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00217|molecule.C00217]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUTDEHYD-RXN`

## Notes

GLT + WATER + NADP -> PROTON + AMMONIUM + 2-KETOGLUTARATE + NADPH; direction=REVERSIBLE
