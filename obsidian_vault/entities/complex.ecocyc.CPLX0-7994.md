---
entity_id: "complex.ecocyc.CPLX0-7994"
entity_type: "complex"
name: "poly-N-acetyl-D-glucosamine synthase"
source_database: "EcoCyc"
source_id: "CPLX0-7994"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-PM-BAC-NEG-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "UDP-<i>N</i>-acetyl-D-glucosamine &beta"
  - "-1,6-N-acetyl-D-glucosaminyl transferase"
  - "PgaCD"
  - "poly-&beta"
  - "-1,6-<i>N</i>-acetyl-D-glucosamine synthase"
  - "PGA synthase"
---

# poly-N-acetyl-D-glucosamine synthase

`complex.ecocyc.CPLX0-7994`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7994`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-PM-BAC-NEG-GN
- Complex type: `regulatory`
- Components: [[protein.P69432|protein.P69432]], [[protein.P75905|protein.P75905]]

## Enriched Summary

PgaCD is a β-glycosyltransferase which polymerises poly-N-acetyl glucosamine (PGA), an adhesin essential in biofilm formation, from an activated UDP-N-acetyl-D-glucosamine (UDP-GlcNAc) precursor and transports it across the inner membrane for deacetylation and export by the OM proteins PgaB and PgaA. PgaC and PgaD form a stable complex . The second messenger C-DI-GMP (c-di-GMP) stimulates PgaC-PgaD interaction and complex stability. c-di-GMP binds concurrently to PgaC-PgaD in vitro and no specific binding is observed in membranes containing only PgaC or PgaD. The binding of c-di-GMP to PgaCD increases in the presence of UDP-GlcNAc . PgaD levels decrease in a strain lacking PgaC but are restored in a c-di-GMP manner when pgaC is expressed from a plasmid. PgaD levels decrease in a strain lacking EG11643-MONOMER. c-di-GMP binds to PgaCD with high affinity, increasing the enzyme's velocity but not its affinity for substrate. c-di-GMP is an allosteric activator and stimulates the glycosyltransferase activity of PgaCD approximately 20-fold in vitro . pgaC and pgaD mutants show reduced biofilm formation and do not accumulate PGA in a crsA background compared to wild-type . PgaC contains 4 predicted trans-membrane domains plus 2 membrane-associated domains; PgaD contains 2 predicted trans-membrane domains. PgaC also contains 2 catalytic domains predicted to be in the cytoplasm...

## Biological Role

Catalyzes RXN0-5413 (reaction.ecocyc.RXN0-5413), TRANS-RXN0-549 (reaction.ecocyc.TRANS-RXN0-549).

## Annotation

PgaCD is a β-glycosyltransferase which polymerises poly-N-acetyl glucosamine (PGA), an adhesin essential in biofilm formation, from an activated UDP-N-acetyl-D-glucosamine (UDP-GlcNAc) precursor and transports it across the inner membrane for deacetylation and export by the OM proteins PgaB and PgaA. PgaC and PgaD form a stable complex . The second messenger C-DI-GMP (c-di-GMP) stimulates PgaC-PgaD interaction and complex stability. c-di-GMP binds concurrently to PgaC-PgaD in vitro and no specific binding is observed in membranes containing only PgaC or PgaD. The binding of c-di-GMP to PgaCD increases in the presence of UDP-GlcNAc . PgaD levels decrease in a strain lacking PgaC but are restored in a c-di-GMP manner when pgaC is expressed from a plasmid. PgaD levels decrease in a strain lacking EG11643-MONOMER. c-di-GMP binds to PgaCD with high affinity, increasing the enzyme's velocity but not its affinity for substrate. c-di-GMP is an allosteric activator and stimulates the glycosyltransferase activity of PgaCD approximately 20-fold in vitro . pgaC and pgaD mutants show reduced biofilm formation and do not accumulate PGA in a crsA background compared to wild-type . PgaC contains 4 predicted trans-membrane domains plus 2 membrane-associated domains; PgaD contains 2 predicted trans-membrane domains. PgaC also contains 2 catalytic domains predicted to be in the cytoplasm. The N and C-termini of both proteins are predicted to be in the cytoplasm . Expression of pgaABCD is higher at 37° C than at 21° C and is highest during stationary phase . Expression also increased in response to one-percent NaCl or ethanol . Expression increased in response to glucose, ethanol, NaCl, and MnCl2 in a clinical isolate, and dramatically increased upon deletion or mutation of csrA in this st

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5413|reaction.ecocyc.RXN0-5413]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-549|reaction.ecocyc.TRANS-RXN0-549]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P69432|protein.P69432]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P75905|protein.P75905]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-7994`
- `QSPROTEOME:QS00187947`

## Notes

1*protein.P69432|1*protein.P75905
