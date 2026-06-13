---
entity_id: "complex.ecocyc.CPLX0-8016"
entity_type: "complex"
name: "UDP-3-O-(3-hydroxymyristoyl)glucosamine N-acyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-8016"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# UDP-3-O-(3-hydroxymyristoyl)glucosamine N-acyltransferase

`complex.ecocyc.CPLX0-8016`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8016`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P21645|protein.P21645]]

## Enriched Summary

UDP-3-O-(3-hydroxymyristoyl)glucosamine N-acetyltransferase (LpxD) catalyzes the third step of lipid IVA biosynthesis, the conversion of UDP-3-O-(3-hydroxymyristoyl)glucosamine to UDP-2,3-bis(3-hydroxymyristoyl)glucosamine . LpxD has specificity for the R-3-OH moiety of R-3-hydroxymyristoyl-ACP, functioning poorly with other fatty acyl moieties . Steady state kinetics and inhibition studies suggest an ordered sequential reaction mechanism. Site directed mutagenesis experiments indicate that H239 is the catalytic base; H276 participates in substrate binding . The M290 residue restricts the size of the hydrophobic cleft that accommodates the acyl substrate and thus limits the substrate range of LpxD . Crystal structures of LpxD alone, interacting with ACP throughout the catalytic cycle, and complexes with peptide and small molecule inhibitors have been solved . The interactions between LpxD, ACP, and ACP's 4'-phosphopantetheine prosthetic group are extensive; a molecular basis for the ordered sequential reaction mechanism of LpxD was proposed . An antibacterial peptide was modeled into the LpxD structure based on data obtained with LpxA . Unphosphorylated EG12147-MONOMER interacts with LpxD and appears to inhibit its function . lpxD temperature-sensitive mutants shed periplasmic proteins, are vulnerable to antibiotics and show signs of disrupted, permeable outer membranes...

## Biological Role

Catalyzes UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN (reaction.ecocyc.UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN).

## Annotation

UDP-3-O-(3-hydroxymyristoyl)glucosamine N-acetyltransferase (LpxD) catalyzes the third step of lipid IVA biosynthesis, the conversion of UDP-3-O-(3-hydroxymyristoyl)glucosamine to UDP-2,3-bis(3-hydroxymyristoyl)glucosamine . LpxD has specificity for the R-3-OH moiety of R-3-hydroxymyristoyl-ACP, functioning poorly with other fatty acyl moieties . Steady state kinetics and inhibition studies suggest an ordered sequential reaction mechanism. Site directed mutagenesis experiments indicate that H239 is the catalytic base; H276 participates in substrate binding . The M290 residue restricts the size of the hydrophobic cleft that accommodates the acyl substrate and thus limits the substrate range of LpxD . Crystal structures of LpxD alone, interacting with ACP throughout the catalytic cycle, and complexes with peptide and small molecule inhibitors have been solved . The interactions between LpxD, ACP, and ACP's 4'-phosphopantetheine prosthetic group are extensive; a molecular basis for the ordered sequential reaction mechanism of LpxD was proposed . An antibacterial peptide was modeled into the LpxD structure based on data obtained with LpxA . Unphosphorylated EG12147-MONOMER interacts with LpxD and appears to inhibit its function . lpxD temperature-sensitive mutants shed periplasmic proteins, are vulnerable to antibiotics and show signs of disrupted, permeable outer membranes . Mutants also show decreased LPS synthesis, reduced activity from the downstream enzyme TETRAACYLDISACC4KIN-MONOMER, and hepta- rather than the normal hexaacylation of the final LPS product . lpxD is an essential gene . LpxD-binding peptides that have antibacterial activity when expressed in the cell were identified , and small molecule inhibitors of LpxD have been characterized . There was some confusi

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN|reaction.ecocyc.UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P21645|protein.P21645]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-8016`
- `QSPROTEOME:QS00206997`

## Notes

3*protein.P21645
