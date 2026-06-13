---
entity_id: "complex.ecocyc.CPLX0-13978"
entity_type: "complex"
name: "DNA-binding transcriptional activator AdiY"
source_database: "EcoCyc"
source_id: "CPLX0-13978"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA-binding transcriptional activator AdiY

`complex.ecocyc.CPLX0-13978`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-13978`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P33234|protein.P33234]]

## Enriched Summary

AdiY is a positive DNA-binding transcriptional regulator that controls the arginine decarboxylase (adi) system, which is strongly induced in rich medium, under anaerobic conditions, and at low pH . Inhibition of adiY expression by CRISPRi reduced cellular fitness under treatment with the antibiotic rifampicin . Several proteins are involved in the induction of the adi system. Changes in the external pH activate the adiA gene. AdiY may function directly or indirectly with CysB to increase expression of adiA. IHF and H-NS might modulate the bending and necessary access of the adiAp promoter for activation . It has also been proposed that AdiY is not the only regulator of the adi system, but the conditions under which AdiY functions remain unknown . The amino acid sequence of AdiY shows homology to members of the XylS/AraC family of transcriptional regulators . The C-terminal region of proteins from this family features a helix-turn-helix motif. AdiY functions as a cytoplasmic pH sensor: it is essentially "off" at physiological pH (~7.4) and becomes active when the intracellular pH drops to mildly acidic values, with its DNA-binding/activation window peaking around pH ~6.3-5.8 (weaker at pH 6.5 and undetectable at pH 5.5 or at >6.7)...

## Annotation

AdiY is a positive DNA-binding transcriptional regulator that controls the arginine decarboxylase (adi) system, which is strongly induced in rich medium, under anaerobic conditions, and at low pH . Inhibition of adiY expression by CRISPRi reduced cellular fitness under treatment with the antibiotic rifampicin . Several proteins are involved in the induction of the adi system. Changes in the external pH activate the adiA gene. AdiY may function directly or indirectly with CysB to increase expression of adiA. IHF and H-NS might modulate the bending and necessary access of the adiAp promoter for activation . It has also been proposed that AdiY is not the only regulator of the adi system, but the conditions under which AdiY functions remain unknown . The amino acid sequence of AdiY shows homology to members of the XylS/AraC family of transcriptional regulators . The C-terminal region of proteins from this family features a helix-turn-helix motif. AdiY functions as a cytoplasmic pH sensor: it is essentially "off" at physiological pH (~7.4) and becomes active when the intracellular pH drops to mildly acidic values, with its DNA-binding/activation window peaking around pH ~6.3-5.8 (weaker at pH 6.5 and undetectable at pH 5.5 or at >6.7) . pH sensing relies on histidine protonation, specifically His34 and His60 in the N-terminal domain; protonation of these residues triggers a reversible conformational change that enables AdiY to bind target promoter DNA as a tetramer . Although AdiY has a putative transmembrane region based on sequence analysis , the pH-sensing mechanism described above supports a one-component cytoplasmic signaling mode . Translation of AdiY is repressed by the small regulatory RNA SgrS; overexpression of AdiY exacerbates the effects of glucose-phosphate stre

## Outgoing Edges (1)

- `activates` --> [[gene.b4115|gene.b4115]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P33234|protein.P33234]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-13978`

## Notes

4*protein.P33234
