---
entity_id: "complex.ecocyc.CPLX-154"
entity_type: "complex"
name: "β-glucoside specific PTS enzyme II / BglG kinase / BglG phosphatase"
source_database: "EcoCyc"
source_id: "CPLX-154"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>bgl</sup>"
  - "Enzyme II<sup>bgl</sup>"
---

# β-glucoside specific PTS enzyme II / BglG kinase / BglG phosphatase

`complex.ecocyc.CPLX-154`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-154`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P08722|protein.P08722]]

## Enriched Summary

BglF belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process known as group translocation (reviewed in . When activated (see below) bglF encodes an Enzyme IIBgl complex which possesses three domains (IIB-IIC-IIA) in a single polypeptide chain. On the basis of sequence similarity BglF belongs to the glucose class of PTS Enzyme IIs . The hydrophilic IIB and IIA domains are localized to the cytoplasmic side of the membrane and contain the active phosphorylation sites - histidine residue 547 in the IIA domain and cysteine residue 24 in the IIB domain . The hydrophobic IIC domain contains eight transmembrane regions and likely forms the sugar translocation channel . Upon activation the aromatic β-glucoside PTS transporter takes up exogenous aryl- and alkyl-β-glucosides (salicin, arbutin and methyl-β-glucoside) releasing the phosphate esters into the cell cytoplasm . Upon activation BglF can also transport and phosphorylate glucose . BglF is a member of the PTS Glucose-Glucoside family of transporters...

## Biological Role

Catalyzes TRANS-RXN-153 (reaction.ecocyc.TRANS-RXN-153), TRANS-RXN-153A (reaction.ecocyc.TRANS-RXN-153A), transport of β-D-glucose by PTS (reaction.ecocyc.TRANS-RXN-157), TRANS-RXN0-518 (reaction.ecocyc.TRANS-RXN0-518). Transports Arbutin (molecule.C06186).

## Annotation

BglF belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process known as group translocation (reviewed in . When activated (see below) bglF encodes an Enzyme IIBgl complex which possesses three domains (IIB-IIC-IIA) in a single polypeptide chain. On the basis of sequence similarity BglF belongs to the glucose class of PTS Enzyme IIs . The hydrophilic IIB and IIA domains are localized to the cytoplasmic side of the membrane and contain the active phosphorylation sites - histidine residue 547 in the IIA domain and cysteine residue 24 in the IIB domain . The hydrophobic IIC domain contains eight transmembrane regions and likely forms the sugar translocation channel . Upon activation the aromatic β-glucoside PTS transporter takes up exogenous aryl- and alkyl-β-glucosides (salicin, arbutin and methyl-β-glucoside) releasing the phosphate esters into the cell cytoplasm . Upon activation BglF can also transport and phosphorylate glucose . BglF is a member of the PTS Glucose-Glucoside family of transporters . The bgl operon contains the bglG gene encoding a bgl operon-specific antiterminator, the blgF gene encoding the Enzyme IIBgl and the bglB gene encoding a phospho-β-glucosidase that hydrolyzes the aglycone from the glycoside phosphate ester . The bgl operon is silent in wild type E. coli K-12 due to the interaction of sequences upstream and downstream of the promoter . It is activated by the insertion of an IS element into the region upstream of the operon in some E. coli isolates as well as by point mutations within the CAP binding site and gyrA or gyrB mutations . FIS helps to silence bgl by blocking act

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-153|reaction.ecocyc.TRANS-RXN-153]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-153A|reaction.ecocyc.TRANS-RXN-153A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-157|reaction.ecocyc.TRANS-RXN-157]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-518|reaction.ecocyc.TRANS-RXN0-518]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C06186|molecule.C06186]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P08722|protein.P08722]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX-154`
- `QSPROTEOME:QS00049690`

## Notes

2*protein.P08722
