---
entity_id: "complex.ecocyc.CPLX-155"
entity_type: "complex"
name: "N,N'-diacetylchitobiose-specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "CPLX-155"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>cel</sup>"
  - "EII<sup>chb</sup>"
  - "Enzyme II<sup>cel</sup>"
  - "Enzyme II <sup>chb</sup>"
---

# N,N'-diacetylchitobiose-specific PTS enzyme II

`complex.ecocyc.CPLX-155`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-155`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P69791|protein.P69791]], [[protein.P17334|protein.P17334]], [[protein.P69795|protein.P69795]]

## Enriched Summary

ChbBCA belongs to the functional superfamily of the PEP-dependent, sugar transporting phosphotransferase system (PTSsugar). The N,N'-diacetylchitobiose (chitobiose) PTS transporter takes up exogenous chitobiose, the β1-4 linked dimer of N-acetylglucosamine and major breakdown product of chitin, releasing the phosphate ester into the cell cytoplasm in preparation for hydrolysis and metabolism, primarily via glycolysis . Diacetylchitobiose, triacetylchitobiose and the non-metabolizable analogue methyl β-diacetylthiochitobiose are all inducers and substrates of the chitobiose permease . The chitobiose PTS transporter requires the general PTS enzymes CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH) as well as Enzyme IIchb for transport and phosphorylation of its substrates . The Enzyme IIchb complex, possesses three polypeptide chains: ChbA, ChbB, and ChbC . It is homologous to the well-characterized lactose-specific PTS Enzyme II of Gram-positive bacteria . ChbC is an integral membrane transport protein while IIA (ChbA) and IIB (ChbB) are soluble . Enzyme IIchb mediates a phosphotransfer and transport reaction whereby a phosphoryl group is transferred from phospho-HPr to ChbA, from ChbA to ChbB and then onto the incoming sugar substrate . ChbCBA is a member of the PTS Lactose - N,N'-diacetylchitobiose-β-glycoside (Lac) family of transporters . E...

## Biological Role

Catalyzes TRANS-RXN-155 (reaction.ecocyc.TRANS-RXN-155), transport of chitobiose (reaction.ecocyc.TRANS-RXN-155B).

## Annotation

ChbBCA belongs to the functional superfamily of the PEP-dependent, sugar transporting phosphotransferase system (PTSsugar). The N,N'-diacetylchitobiose (chitobiose) PTS transporter takes up exogenous chitobiose, the β1-4 linked dimer of N-acetylglucosamine and major breakdown product of chitin, releasing the phosphate ester into the cell cytoplasm in preparation for hydrolysis and metabolism, primarily via glycolysis . Diacetylchitobiose, triacetylchitobiose and the non-metabolizable analogue methyl β-diacetylthiochitobiose are all inducers and substrates of the chitobiose permease . The chitobiose PTS transporter requires the general PTS enzymes CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH) as well as Enzyme IIchb for transport and phosphorylation of its substrates . The Enzyme IIchb complex, possesses three polypeptide chains: ChbA, ChbB, and ChbC . It is homologous to the well-characterized lactose-specific PTS Enzyme II of Gram-positive bacteria . ChbC is an integral membrane transport protein while IIA (ChbA) and IIB (ChbB) are soluble . Enzyme IIchb mediates a phosphotransfer and transport reaction whereby a phosphoryl group is transferred from phospho-HPr to ChbA, from ChbA to ChbB and then onto the incoming sugar substrate . ChbCBA is a member of the PTS Lactose - N,N'-diacetylchitobiose-β-glycoside (Lac) family of transporters . E. coli is chemotactic towards chitobiose . The chb operon contains in addition to chbBCA, the EG10143 "chbR" gene, which encodes a negative regulatory protein, the EG10144 "chbF" gene encoding an enzyme that functions as an acetylchitobiose-6-phosphate hydrolase and the EG12198 "chbG" encoding a chitooligosaccharide deacetylase. The operon gene order is chbBCARFG. The chb operon is subject to complex regulation by three tr

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-155|reaction.ecocyc.TRANS-RXN-155]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-155B|reaction.ecocyc.TRANS-RXN-155B]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P17334|protein.P17334]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69791|protein.P69791]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69795|protein.P69795]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX-155`
- `PDB:2WY2`
- `PDB:2WWV`
- `QSPROTEOME:QS00049469`

## Notes

1*protein.P69791|1*protein.P17334|1*protein.P69795
