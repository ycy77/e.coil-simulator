---
entity_id: "complex.ecocyc.BCCP-CPLX"
entity_type: "complex"
name: "biotin carboxyl carrier protein (dimer)"
source_database: "EcoCyc"
source_id: "BCCP-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "BCCP"
  - "AccB"
---

# biotin carboxyl carrier protein (dimer)

`complex.ecocyc.BCCP-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:BCCP-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.ecocyc.BCCP-BIOTIN|protein.ecocyc.BCCP-BIOTIN]]

## Enriched Summary

Biotin carboxyl carrier protein (BCCP) plays a central role in the acetyl-CoA carboxylase complex. The overall carboxylase reaction takes place in two distinct half-reactions. BCCP, which contains a biotinyl prosthetic group covalently attached to a specific lysyl residue, is carboxylated in the first partial reaction. In the second partial reaction the carboxyl group is transferred to an acceptor and BCCP is regenerated for further carboxylation . On the other hand, BCCP amino terminal is able to bind to DNA; this means, BCCP autoregulates its coding gene expression (the accBD operon) . Biotin carboxyl carrier protein (BCCP) plays a central role in the acetyl-CoA carboxylase complex. The overall carboxylase reaction takes place in two distinct half-reactions. BCCP, which contains a biotinyl prosthetic group covalently attached to a specific lysyl residue, is carboxylated in the first partial reaction. In the second partial reaction the carboxyl group is transferred to an acceptor and BCCP is regenerated for further carboxylation . On the other hand, BCCP amino terminal is able to bind to DNA; this means, BCCP autoregulates its coding gene expression (the accBD operon) .

## Biological Role

Component of acetyl-CoA carboxylase complex (complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX).

## Annotation

Biotin carboxyl carrier protein (BCCP) plays a central role in the acetyl-CoA carboxylase complex. The overall carboxylase reaction takes place in two distinct half-reactions. BCCP, which contains a biotinyl prosthetic group covalently attached to a specific lysyl residue, is carboxylated in the first partial reaction. In the second partial reaction the carboxyl group is transferred to an acceptor and BCCP is regenerated for further carboxylation . On the other hand, BCCP amino terminal is able to bind to DNA; this means, BCCP autoregulates its coding gene expression (the accBD operon) .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX|complex.ecocyc.ACETYL-COA-CARBOXYLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.ecocyc.BCCP-BIOTIN|protein.ecocyc.BCCP-BIOTIN]] `EcoCyc` `database` - EcoCyc component coefficient=2

## External IDs

- `EcoCyc:BCCP-CPLX`
- `QSPROTEOME:QS00049577`

## Notes

2*protein.ecocyc.BCCP-BIOTIN
