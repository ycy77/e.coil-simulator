---
entity_id: "protein.P0A6I0"
entity_type: "protein"
name: "cmk"
source_database: "UniProt"
source_id: "P0A6I0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cmk mssA ycaF ycaG b0910 JW0893"
---

# cmk

`protein.P0A6I0`

## Static

- Type: `protein`
- Source: `UniProt:P0A6I0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: ATP, dATP, and GTP are equally effective as phosphate donors. CMP and dCMP are the best phosphate acceptors. {ECO:0000269|PubMed:7836281, ECO:0000269|PubMed:8190075}. Cytidylate kinase (Cmk) rephosphorylates CMP and dCMP that is produced by the turnover of nucleic acids and CDP diglycerides. Cmk is not an essential enzyme, because CMP is not an intermediate in the de novo pathway for the synthesis of CTP. Unlike the eukaryotic UMP/CMP kinases, this enzyme is specific for CMP or dCMP. Cytidylate kinase affects the rate of 5'-end-dependent mRNA degradation by acting together with DIAMINOPIMEPIM-MONOMER DapF to stimulate the activity of G7459-MONOMER RppH; in addition, by reducing the concentration of CMP in the cell, the synthesis of transcripts beginning with monophosphorylated cytidine is reduced . Cmk appears to have some peptidyl-prolyl cis-trans isomerase activity . Crystal strutures of Cmk have been solved . They dynamic properties of the ATP binding site were probed with a fluorescent dATP analog, and molecular modeling suggested that ATP-mediated induced fit is modulated by CMP binding, which leads to a closed conformation of the active site . Residues involved in the interaction with the pentose moiety and the pyrimidine ring of CMP have been identified in the crystal structure and functionally verified by site-directed mutagenesis...

## Biological Role

Catalyzes ATP:CMP phosphotransferase (reaction.R00512), RXN-11832 (reaction.ecocyc.RXN-11832), RXN-7913 (reaction.ecocyc.RXN-7913). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: ATP, dATP, and GTP are equally effective as phosphate donors. CMP and dCMP are the best phosphate acceptors. {ECO:0000269|PubMed:7836281, ECO:0000269|PubMed:8190075}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00512|reaction.R00512]] `KEGG` `database` - via EC:2.7.4.25
- `catalyzes` --> [[reaction.ecocyc.RXN-11832|reaction.ecocyc.RXN-11832]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-7913|reaction.ecocyc.RXN-7913]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0910|gene.b0910]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6I0`
- `KEGG:ecj:JW0893;eco:b0910;ecoc:C3026_05610;`
- `GeneID:93776507;945535;`
- `GO:GO:0005524; GO:0005829; GO:0006220; GO:0010165; GO:0015949; GO:0036430; GO:0036431; GO:0097216`
- `EC:2.7.4.25`

## Notes

Cytidylate kinase (CK) (EC 2.7.4.25) (Cytidine monophosphate kinase) (CMP kinase) (Protein MssA) (p25)
