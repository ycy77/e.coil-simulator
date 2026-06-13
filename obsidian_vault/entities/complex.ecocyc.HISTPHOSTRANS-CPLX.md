---
entity_id: "complex.ecocyc.HISTPHOSTRANS-CPLX"
entity_type: "complex"
name: "histidinol-phosphate aminotransferase"
source_database: "EcoCyc"
source_id: "HISTPHOSTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# histidinol-phosphate aminotransferase

`complex.ecocyc.HISTPHOSTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:HISTPHOSTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P06986|protein.P06986]]

## Enriched Summary

Histidinol-phosphate aminotransferase (HisC) catalyzes the seventh step in the biosynthesis of histidine. HisC catalyzes the conversion of imidazole acetol-phosphate to histidinol-phosphate . A number of crystal structures have been determined for the functional HisC dimer. HisC has been crystallized on its own to 2 Å, with histidinol-phosphate to 2.2 Å and with N-(5'-phosphopyridoxyl)-L-glutamate to 2.3 Å . It has also been crystallized with pyridoxamine-5'-phosphate to 1.5 Å, as an internal aldimine with pyridoxal-5'-phosphate to 2.2 Å and in a covalent complex with pyridoxal-5'-phosphate and L-histidinol to 2.2 Å . Spectroscopic and pK(a) analyses of HisC have also been carried out . HisC expression levels were elevated when grown anaerobically at high pH . A temperature-sensitive mutation in this gene was identified that showed potential as a growth-switch for genetic engineering . Histidinol-phosphate aminotransferase (HisC) catalyzes the seventh step in the biosynthesis of histidine. HisC catalyzes the conversion of imidazole acetol-phosphate to histidinol-phosphate . A number of crystal structures have been determined for the functional HisC dimer. HisC has been crystallized on its own to 2 Å, with histidinol-phosphate to 2.2 Å and with N-(5'-phosphopyridoxyl)-L-glutamate to 2.3 Å . It has also been crystallized with pyridoxamine-5'-phosphate to 1...

## Biological Role

Catalyzes HISTAMINOTRANS-RXN (reaction.ecocyc.HISTAMINOTRANS-RXN).

## Annotation

Histidinol-phosphate aminotransferase (HisC) catalyzes the seventh step in the biosynthesis of histidine. HisC catalyzes the conversion of imidazole acetol-phosphate to histidinol-phosphate . A number of crystal structures have been determined for the functional HisC dimer. HisC has been crystallized on its own to 2 Å, with histidinol-phosphate to 2.2 Å and with N-(5'-phosphopyridoxyl)-L-glutamate to 2.3 Å . It has also been crystallized with pyridoxamine-5'-phosphate to 1.5 Å, as an internal aldimine with pyridoxal-5'-phosphate to 2.2 Å and in a covalent complex with pyridoxal-5'-phosphate and L-histidinol to 2.2 Å . Spectroscopic and pK(a) analyses of HisC have also been carried out . HisC expression levels were elevated when grown anaerobically at high pH . A temperature-sensitive mutation in this gene was identified that showed potential as a growth-switch for genetic engineering .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.HISTAMINOTRANS-RXN|reaction.ecocyc.HISTAMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P06986|protein.P06986]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:HISTPHOSTRANS-CPLX`
- `QSPROTEOME:QS00199195`

## Notes

2*protein.P06986
