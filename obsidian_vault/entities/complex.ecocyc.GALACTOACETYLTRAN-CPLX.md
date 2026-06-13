---
entity_id: "complex.ecocyc.GALACTOACETYLTRAN-CPLX"
entity_type: "complex"
name: "galactoside O-acetyltransferase"
source_database: "EcoCyc"
source_id: "GALACTOACETYLTRAN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# galactoside O-acetyltransferase

`complex.ecocyc.GALACTOACETYLTRAN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GALACTOACETYLTRAN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P07464|protein.P07464]]

## Enriched Summary

Galactoside O-acetyltransferase (GAT) encoded by lacA catalyzes the transfer of an acetyl group from acetyl-CoA to the 6-hydroxyl of some galactopyranosides. The enzyme has broad substrate specificity and will acetylate galactosides, thiogalactosides, glucosides and lactosides. Its exact physiological function is uncertain but it may act as a detoxifying enzyme, acetylating non-metabolizable sugars to prevent their re-entry into the cell . LacA, along with LacZ and LacY, are products of the well-studied lac operon. In early work, GAT activity was observed . It was partially purified from extracts of E. coli ML 308 and shown to efficiently transfer the acetyl group of acetyl-CoA to acceptors such as isopropyl-thio-β-D-galactopyranoside (IPTG) and several other substituted galactosides and glucosides. It preferred acetyl-CoA as donor when compared with butyryl-CoA, succinyl-CoA and palmityl-CoA . This enzyme was crystallized and further characterized biochemically . A spectrophotometric assay using 5,5'-dithio-bis-2-nitrobenzoate , and an affinity chromatography purification procedure , were established. GAT from an E. coli K-12 strain was also purified, characterized kinetically, and p-nitrophenyl β-D-galactoside was shown to be an efficient substrate...

## Biological Role

Catalyzes GALACTOACETYLTRAN-RXN (reaction.ecocyc.GALACTOACETYLTRAN-RXN).

## Annotation

Galactoside O-acetyltransferase (GAT) encoded by lacA catalyzes the transfer of an acetyl group from acetyl-CoA to the 6-hydroxyl of some galactopyranosides. The enzyme has broad substrate specificity and will acetylate galactosides, thiogalactosides, glucosides and lactosides. Its exact physiological function is uncertain but it may act as a detoxifying enzyme, acetylating non-metabolizable sugars to prevent their re-entry into the cell . LacA, along with LacZ and LacY, are products of the well-studied lac operon. In early work, GAT activity was observed . It was partially purified from extracts of E. coli ML 308 and shown to efficiently transfer the acetyl group of acetyl-CoA to acceptors such as isopropyl-thio-β-D-galactopyranoside (IPTG) and several other substituted galactosides and glucosides. It preferred acetyl-CoA as donor when compared with butyryl-CoA, succinyl-CoA and palmityl-CoA . This enzyme was crystallized and further characterized biochemically . A spectrophotometric assay using 5,5'-dithio-bis-2-nitrobenzoate , and an affinity chromatography purification procedure , were established. GAT from an E. coli K-12 strain was also purified, characterized kinetically, and p-nitrophenyl β-D-galactoside was shown to be an efficient substrate . Chemical modification studies suggested that His115 is catalytically important and site-directed mutagenesis studies suggested that Tyr83 is essential for catalytic activity . GAT was initially thought to be a homodimer , but later crosslinking studies showed it to be a homotrimer . Antisense RNA for the lacA mRNA was used in an early demonstration of the antisense technique to block the translation of specific messenger RNAs . The influence of GAT, which acetylates and inactivates IPTG, on lac operon induction behavior w

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GALACTOACETYLTRAN-RXN|reaction.ecocyc.GALACTOACETYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P07464|protein.P07464]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:GALACTOACETYLTRAN-CPLX`
- `QSPROTEOME:QS00183041`

## Notes

3*protein.P07464
