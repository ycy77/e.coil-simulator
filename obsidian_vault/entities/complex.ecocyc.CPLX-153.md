---
entity_id: "complex.ecocyc.CPLX-153"
entity_type: "complex"
name: "β-glucoside specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "CPLX-153"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EIIBC<sup>asc</sup>"
  - "Enzyme IIBC<sup>asc</sup>"
---

# β-glucoside specific PTS enzyme II

`complex.ecocyc.CPLX-153`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-153`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P24241|protein.P24241]]

## Enriched Summary

AscF belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar sustrates in a process known as group translocation (reviewed in . When activated (see below) ascF encodes an Enzyme IIBCAsc complex. AscF possesses two domains in a single polypeptide chain with the domain order IIB-IIC. It is homologous to PtsG (the glucose-specific PTS Enzyme II) which has been reported to possess 8 transmembrane α-helical segments in its IIC domain. In order for transport to occur, a IIA domain from another PTS transport system, such as IIAGlc, would be required to transfer the phosphate from PTSH-MONOMER "HPr" to IIBAsc . The specific IIA domain that associates with the cryptic β-glucoside PTS transporter has not been identified. AscF is a member of the PTS Glucose-Glucoside family of transporters . The asc operon contains the ascF gene encoding the Enzyme IIBCAsc and the ascB gene encoding a phospho-β-glucosidase that hydrolyzes the aglycone from the glycoside phosphate ester . Monocistronic EG10087 "ascG", encoding a transcriptional repressor of the ascFB operon, and the ascFB operon are transcribed from divergent promoters . The asc operon is cryptic in wild type E. coli K-12 . It can be activated by the insertion of IS186 into ascG in some E...

## Biological Role

Catalyzes TRANS-RXN-153 (reaction.ecocyc.TRANS-RXN-153), TRANS-RXN-153A (reaction.ecocyc.TRANS-RXN-153A), TRANS-RXN-155 (reaction.ecocyc.TRANS-RXN-155).

## Annotation

AscF belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar sustrates in a process known as group translocation (reviewed in . When activated (see below) ascF encodes an Enzyme IIBCAsc complex. AscF possesses two domains in a single polypeptide chain with the domain order IIB-IIC. It is homologous to PtsG (the glucose-specific PTS Enzyme II) which has been reported to possess 8 transmembrane α-helical segments in its IIC domain. In order for transport to occur, a IIA domain from another PTS transport system, such as IIAGlc, would be required to transfer the phosphate from PTSH-MONOMER "HPr" to IIBAsc . The specific IIA domain that associates with the cryptic β-glucoside PTS transporter has not been identified. AscF is a member of the PTS Glucose-Glucoside family of transporters . The asc operon contains the ascF gene encoding the Enzyme IIBCAsc and the ascB gene encoding a phospho-β-glucosidase that hydrolyzes the aglycone from the glycoside phosphate ester . Monocistronic EG10087 "ascG", encoding a transcriptional repressor of the ascFB operon, and the ascFB operon are transcribed from divergent promoters . The asc operon is cryptic in wild type E. coli K-12 . It can be activated by the insertion of IS186 into ascG in some E. coli isolates . Crypticity of this and other E. coli β-glucoside metabolic operons presumably serves as a protective device against toxic β-glucosides found in nature . Decryptified asc mutants are able to utilize arbutin, salicin, and, to a lesser extent, cellobiose as sole carbon and energy sources . ascG deletion strains have a positive response to arbutin and salicin in Biolog phenotype microar

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-153|reaction.ecocyc.TRANS-RXN-153]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-153A|reaction.ecocyc.TRANS-RXN-153A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-155|reaction.ecocyc.TRANS-RXN-155]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P24241|protein.P24241]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX-153`
- `QSPROTEOME:QS00200449`

## Notes

2*protein.P24241
