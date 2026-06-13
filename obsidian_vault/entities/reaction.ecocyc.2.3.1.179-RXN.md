---
entity_id: "reaction.ecocyc.2.3.1.179-RXN"
entity_type: "reaction"
name: "2.3.1.179-RXN"
source_database: "EcoCyc"
source_id: "2.3.1.179-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.3.1.179-RXN

`reaction.ecocyc.2.3.1.179-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.3.1.179-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Involved in the dissociated (or type II) fatty acid biosynthesis system that occurs in plants and bacteria. While the substrate specificity of this enzyme is very similar to that of EC 2.3.1.41, it differs in that palmitoleoyl-ACP is not a good substrate of EC 2.3.1.41 but is an excellent substrate of this enzyme. The fatty-acid composition of Escherichia coli changes as a function of growth temperature, with the proportion of unsaturated fatty acids increasing with lower growth temperature. Controls the temperature-dependent regulation of fatty-acid composition, with mutants lacking this acivity being deficient in the elongation of palmitoleate to cis-vaccenate at low temperatures. EcoCyc reaction equation: Palmitoleoyl-ACPs + MALONYL-ACP + PROTON -> 3-oxo-cis-vaccenoyl-ACPs + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT. Involved in the dissociated (or type II) fatty acid biosynthesis system that occurs in plants and bacteria. While the substrate specificity of this enzyme is very similar to that of EC 2.3.1.41, it differs in that palmitoleoyl-ACP is not a good substrate of EC 2.3.1.41 but is an excellent substrate of this enzyme. The fatty-acid composition of Escherichia coli changes as a function of growth temperature, with the proportion of unsaturated fatty acids increasing with lower growth temperature...

## Biological Role

Catalyzed by 3-oxoacyl-[acyl carrier protein] synthase 2 (complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX). Substrates: H+ (molecule.C00080). Products: CO2 (molecule.C00011).

## Enriched Pathways

- `ecocyc.PWY-5973` cis-vaccenate biosynthesis (EcoCyc)

## Annotation

Involved in the dissociated (or type II) fatty acid biosynthesis system that occurs in plants and bacteria. While the substrate specificity of this enzyme is very similar to that of EC 2.3.1.41, it differs in that palmitoleoyl-ACP is not a good substrate of EC 2.3.1.41 but is an excellent substrate of this enzyme. The fatty-acid composition of Escherichia coli changes as a function of growth temperature, with the proportion of unsaturated fatty acids increasing with lower growth temperature. Controls the temperature-dependent regulation of fatty-acid composition, with mutants lacking this acivity being deficient in the elongation of palmitoleate to cis-vaccenate at low temperatures.

## Pathways

- `ecocyc.PWY-5973` cis-vaccenate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX|complex.ecocyc.3-OXOACYL-ACP-SYNTHII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.3.1.179-RXN`

## Notes

Palmitoleoyl-ACPs + MALONYL-ACP + PROTON -> 3-oxo-cis-vaccenoyl-ACPs + CARBON-DIOXIDE + ACP; direction=LEFT-TO-RIGHT
