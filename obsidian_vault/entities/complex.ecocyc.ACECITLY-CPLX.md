---
entity_id: "complex.ecocyc.ACECITLY-CPLX"
entity_type: "complex"
name: "citrate lyase"
source_database: "EcoCyc"
source_id: "ACECITLY-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "citrate lyase, active"
  - "acetyl-citrate lyase"
---

# citrate lyase

`complex.ecocyc.ACECITLY-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACECITLY-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P69330|protein.P69330]], [[protein.P75726|protein.P75726]], [[protein.P0A9I1|protein.P0A9I1]]

## Enriched Summary

Citrate lyase, an anaerobic enzyme, catalyzes the cleavage of citrate to acetate and oxaloacetate . The citrate molecule is very stable, and needs to be activated prior to cleavage by forming a thioester bond with the enzyme. The enzyme is a complex of three subunits, one of them a dedicated acyl carrier protein (acp). It is synthesized in an apo form, and is converted to its holo form by the covalent binding of the unusual prosthetic group 2-5-PHOSPHORIBOSYL-3-DEPHOSPHO-COA to the [acp] component, resulting in DEACETYL-CITRATE-LYASE. However, this holo form is still not fully active - in order to be active, the prosthetic group needs to be acetylated, a reaction catalyzed by CITC-MONOMER, which generates CITRATE-LYASE. The α subunit of the ACECITLY-CPLX is a citrate-[acp] transferase that catalyzes the exchange of the bound acetyl group with a citrate molecule, generating Citrate-Lyase-Citryl-Forms and releasing an ACET molecule. The β subunit, which is a citryl-[acp] lyase, catalyzes the subsequent step, cleaving the bound citryl group, releasing OXALACETIC_ACID and regenerating CITRATE-LYASE. All three subunits are required for the reaction to take place . Wild-type E. coli K-12 does not have active citrate lyase activity. Mutants defective in molybdenum cofactor synthesis have active citrate lyase...

## Biological Role

Catalyzes CITLY-RXN (reaction.ecocyc.CITLY-RXN), CITRYLY-RXN (reaction.ecocyc.CITRYLY-RXN), CITTRANS-RXN (reaction.ecocyc.CITTRANS-RXN). Bound by Magnesium cation (molecule.C00305), 2'-(5''-phosphoribosyl)-3'-dephospho-CoA (molecule.ecocyc.2-5-PHOSPHORIBOSYL-3-DEPHOSPHO-COA).

## Annotation

Citrate lyase, an anaerobic enzyme, catalyzes the cleavage of citrate to acetate and oxaloacetate . The citrate molecule is very stable, and needs to be activated prior to cleavage by forming a thioester bond with the enzyme. The enzyme is a complex of three subunits, one of them a dedicated acyl carrier protein (acp). It is synthesized in an apo form, and is converted to its holo form by the covalent binding of the unusual prosthetic group 2-5-PHOSPHORIBOSYL-3-DEPHOSPHO-COA to the [acp] component, resulting in DEACETYL-CITRATE-LYASE. However, this holo form is still not fully active - in order to be active, the prosthetic group needs to be acetylated, a reaction catalyzed by CITC-MONOMER, which generates CITRATE-LYASE. The α subunit of the ACECITLY-CPLX is a citrate-[acp] transferase that catalyzes the exchange of the bound acetyl group with a citrate molecule, generating Citrate-Lyase-Citryl-Forms and releasing an ACET molecule. The β subunit, which is a citryl-[acp] lyase, catalyzes the subsequent step, cleaving the bound citryl group, releasing OXALACETIC_ACID and regenerating CITRATE-LYASE. All three subunits are required for the reaction to take place . Wild-type E. coli K-12 does not have active citrate lyase activity. Mutants defective in molybdenum cofactor synthesis have active citrate lyase . purified the enzyme from Crooke's strain (ATCC 8739), which is not a K-12 strain.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.CITLY-RXN|reaction.ecocyc.CITLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CITRYLY-RXN|reaction.ecocyc.CITRYLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CITTRANS-RXN|reaction.ecocyc.CITTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.2-5-PHOSPHORIBOSYL-3-DEPHOSPHO-COA|molecule.ecocyc.2-5-PHOSPHORIBOSYL-3-DEPHOSPHO-COA]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9I1|protein.P0A9I1]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` <-- [[protein.P69330|protein.P69330]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` <-- [[protein.P75726|protein.P75726]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:ACECITLY-CPLX`

## Notes

6*protein.P69330|6*protein.P75726|6*protein.P0A9I1
