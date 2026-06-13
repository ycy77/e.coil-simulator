---
entity_id: "complex.ecocyc.CPLX0-8219"
entity_type: "complex"
name: "thiosulfate sulfurtransferase YgaP"
source_database: "EcoCyc"
source_id: "CPLX0-8219"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# thiosulfate sulfurtransferase YgaP

`complex.ecocyc.CPLX0-8219`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8219`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P55734|protein.P55734]]

## Enriched Summary

YgaP is an inner membrane protein with two predicted transmembrane domains. The C terminus is located in the cytoplasm . The YgaP protein has rhodanese activity in vitro (Ahmed, F., Ph.D. Thesis, cited in ). YgaP contains a cytoplasmic rhodanese domain (residues 1-118) with sulfurtransferase activity plus a C-terminal domain (residues 119-174) containing two transmembrane helices. A solution structure of the rhodanese domain showed a typical αβ rhodanese fold consisting of 5 α-helices and 5 β-strands which fold into an α-β-α sandwich. The rhodanese domain of YgaP contains a thiosulfate active site containing a catalytic cysteine residue (Cys64) which catalyses the transfer of sulfur from thiosulfate to cyanide to form thiocyanate in vitro . A full length YgaP(C159S) mutant forms a dimer when reconstituted in detergent micelles. Thiocyanate induced conformational change in the transmembrane domain (TMD) of purified YgaP(C159S) solubilized in detergent or reconstituted in proteoliposomes has been observed, leading to speculation of an additional role in thiocyanate export...

## Biological Role

Catalyzes THIOSULFATE-SULFURTRANSFERASE-RXN (reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN).

## Annotation

YgaP is an inner membrane protein with two predicted transmembrane domains. The C terminus is located in the cytoplasm . The YgaP protein has rhodanese activity in vitro (Ahmed, F., Ph.D. Thesis, cited in ). YgaP contains a cytoplasmic rhodanese domain (residues 1-118) with sulfurtransferase activity plus a C-terminal domain (residues 119-174) containing two transmembrane helices. A solution structure of the rhodanese domain showed a typical αβ rhodanese fold consisting of 5 α-helices and 5 β-strands which fold into an α-β-α sandwich. The rhodanese domain of YgaP contains a thiosulfate active site containing a catalytic cysteine residue (Cys64) which catalyses the transfer of sulfur from thiosulfate to cyanide to form thiocyanate in vitro . A full length YgaP(C159S) mutant forms a dimer when reconstituted in detergent micelles. Thiocyanate induced conformational change in the transmembrane domain (TMD) of purified YgaP(C159S) solubilized in detergent or reconstituted in proteoliposomes has been observed, leading to speculation of an additional role in thiocyanate export . The rhodanese domain is connected to the TMD by a flexible linker; the two transmembrane regions form the homodimer interface; thiocyanate binding is associated with conformational change in the transmembrane regions The rhodanese domain of overexpressed YgaP may be S-nitrosylated in vivo; the site of nitrosylation is Cys64; S-nitrosylation competes with S-sulfhydration and S-nitrosylation of Cys64 inactivates the sulfur transferase activity of the rhodanese domain in vitro; S-nitrosylation induces structural and dynamical changes in the rhodanese domain . Expression of ygaVP is inducible by tributylin (TBT), a compound that was widely used as a preservation agent .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN|reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P55734|protein.P55734]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8219`
- `QSPROTEOME:QS00203785`

## Notes

2*protein.P55734
