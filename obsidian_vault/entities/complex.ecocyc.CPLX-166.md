---
entity_id: "complex.ecocyc.CPLX-166"
entity_type: "complex"
name: "mannitol-specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "CPLX-166"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EIIMtl"
---

# mannitol-specific PTS enzyme II

`complex.ecocyc.CPLX-166`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-166`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P00550|protein.P00550]]

## Enriched Summary

MtlA, the mannitol PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in ). MtlA takes up exogenous mannitol, releasing the phosphate ester, mannitol-1-P, into the cell cytoplasm in preparation for oxidation to fructose-6-P by the NAD-dependent mannitol-P dehydrogenase (MtlD) and subsequent metabolism via glycolysis (MANNIDEG-PWY). Purified MtlA transports D-glucitol and D-arabitol with low efficiency . MtlA, the Enzyme IIMtl complex, possesses three domains in a single polypeptide chain with the domain order IIC-IIB-IIA. MtlA consists of an N-terminal hydrophobic domain (IIC) that resides in the inner membrane and a C-terminal, hydrophilic domain (IIBA) that is located on the cytoplasmic side of the membrane . Histidine 554 and cysteine 384 located in the hydrophilic domain are the phosphotransfer sites. His554 accepts a phosphoryl group from the cytoplasmic HPr protein; Cys384 is the site of phosphotransfer to D-mannitol . The N-terminal domain of MtlA contains 6 transmembrane α-helical segments and is responsible for binding and translocation of mannitol . MtlA functions as a homodimer...

## Biological Role

Catalyzes D-mannitol PTS permease (reaction.ecocyc.TRANS-RXN-156), TRANS-RXN-169 (reaction.ecocyc.TRANS-RXN-169).

## Annotation

MtlA, the mannitol PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in ). MtlA takes up exogenous mannitol, releasing the phosphate ester, mannitol-1-P, into the cell cytoplasm in preparation for oxidation to fructose-6-P by the NAD-dependent mannitol-P dehydrogenase (MtlD) and subsequent metabolism via glycolysis (MANNIDEG-PWY). Purified MtlA transports D-glucitol and D-arabitol with low efficiency . MtlA, the Enzyme IIMtl complex, possesses three domains in a single polypeptide chain with the domain order IIC-IIB-IIA. MtlA consists of an N-terminal hydrophobic domain (IIC) that resides in the inner membrane and a C-terminal, hydrophilic domain (IIBA) that is located on the cytoplasmic side of the membrane . Histidine 554 and cysteine 384 located in the hydrophilic domain are the phosphotransfer sites. His554 accepts a phosphoryl group from the cytoplasmic HPr protein; Cys384 is the site of phosphotransfer to D-mannitol . The N-terminal domain of MtlA contains 6 transmembrane α-helical segments and is responsible for binding and translocation of mannitol . MtlA functions as a homodimer . MtlA is an asymmetric dimer MtlA contains one high affinity mannitol binding site and one low affinity binding site . Unphosphorylated MtlA contains one high affinity mannitol binding site . The mannitol binding site is located in the middle of the membrane - this is also the site where mannitol is phosphorylated . Phosphotransfer from His554 to Cys384 occurs between subunits in a permease dimer . MtlA is a member of the PTS Fructose-Mannitol (Fru) family o

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-156|reaction.ecocyc.TRANS-RXN-156]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-169|reaction.ecocyc.TRANS-RXN-169]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P00550|protein.P00550]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX-166`
- `QSPROTEOME:QS00049691`

## Notes

2*protein.P00550
