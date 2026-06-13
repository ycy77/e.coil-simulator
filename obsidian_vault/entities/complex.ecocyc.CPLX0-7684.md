---
entity_id: "complex.ecocyc.CPLX0-7684"
entity_type: "complex"
name: "L-valine exporter"
source_database: "EcoCyc"
source_id: "CPLX0-7684"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "YgaZ/YgaH L-valine exporter complex"
---

# L-valine exporter

`complex.ecocyc.CPLX0-7684`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7684`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76630|protein.P76630]], [[protein.P43667|protein.P43667]]

## Enriched Summary

YgaZ and YgaH comprise a putative two-component transporter that is implicated in L-valine export in E. coli K-12. YgaZ and YgaH are homologs of the BrnF and BrnE proteins respectively of the Corynebacterium glutamicum methionine/branched chain amino acid export system . A ygaZH knockout strain of E. coli K-12 W3110 has decreased resistance to the L-valine analog, DL-norvaline, while overexpression of ygaZH results in significantly increased resistance compared to wild type . Overexpression of ygaZH increases L-valine production in an engineered L-valine producing strain; deletion of ygaZH does not affect L-valine production suggesting that YgaZH may not be the major L-valine exporter in the engineered strain . In the Transporter Classification Database YgaZH is a member of the Branched Chain Amino Acid Exporter (LIV-E) family. Expression of ygaZH is induced by PD00353 "Lrp" in the presence of L-valine . ygaZ and ygaH are 'core pH-dependent genes' - expression is upregulated at basic pH in both aerobic and oxygen limited conditions . YgaZ and YgaH comprise a putative two-component transporter that is implicated in L-valine export in E. coli K-12. YgaZ and YgaH are homologs of the BrnF and BrnE proteins respectively of the Corynebacterium glutamicum methionine/branched chain amino acid export system . A ygaZH knockout strain of E...

## Biological Role

Catalyzes TRANS-RXN0-269 (reaction.ecocyc.TRANS-RXN0-269).

## Annotation

YgaZ and YgaH comprise a putative two-component transporter that is implicated in L-valine export in E. coli K-12. YgaZ and YgaH are homologs of the BrnF and BrnE proteins respectively of the Corynebacterium glutamicum methionine/branched chain amino acid export system . A ygaZH knockout strain of E. coli K-12 W3110 has decreased resistance to the L-valine analog, DL-norvaline, while overexpression of ygaZH results in significantly increased resistance compared to wild type . Overexpression of ygaZH increases L-valine production in an engineered L-valine producing strain; deletion of ygaZH does not affect L-valine production suggesting that YgaZH may not be the major L-valine exporter in the engineered strain . In the Transporter Classification Database YgaZH is a member of the Branched Chain Amino Acid Exporter (LIV-E) family. Expression of ygaZH is induced by PD00353 "Lrp" in the presence of L-valine . ygaZ and ygaH are 'core pH-dependent genes' - expression is upregulated at basic pH in both aerobic and oxygen limited conditions .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-269|reaction.ecocyc.TRANS-RXN0-269]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P43667|protein.P43667]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P76630|protein.P76630]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-7684`
- `QSPROTEOME:QS00049435`

## Notes

protein.P76630|protein.P43667
