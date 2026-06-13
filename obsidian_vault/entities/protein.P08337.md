---
entity_id: "protein.P08337"
entity_type: "protein"
name: "mutT"
source_database: "UniProt"
source_id: "P08337"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mutT b0099 JW0097"
---

# mutT

`protein.P08337`

## Static

- Type: `protein`
- Source: `UniProt:P08337`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Specifically hydrolyzes both 8-oxo-deoxyguanosine triphosphate (8-oxo-dGTP) and 8-oxo-guanosine triphosphate (8-oxo-GTP) to the related monophosphates, thereby cleaning up the nucleotide pools and preventing misincorporation of 8-oxoGua into DNA and RNA (PubMed:1309939, PubMed:15850400, PubMed:9311918). It prevents replicational errors by removing an oxidatively damaged form of guanine (8-oxo-dGTP) from DNA and the nucleotide pool (PubMed:1309939). 8-oxo-dGTP can be inserted opposite dA and dC residues of template DNA with almost equal efficiency thus leading to A.T to G.C transversions (PubMed:1309939). MutT may also ensure transcriptional fidelity, removing 8-oxo-GTP from the ribonucleotide triphosphate pool (PubMed:9311918). However, due to the lower efficiency of RNA polymerase 8-oxo-GTP incorporation, MutT is probably not a major contributor to transcriptional fidelity (PubMed:25294823). It also hydrolyzes 8-oxo-dGDP and 8-oxo-GDP to their monophosphate form (PubMed:15850400). In vitro, can also use dGTP, dGDP and other various nucleoside di- and triphosphates, with much lower efficiency (PubMed:1309939, PubMed:15850400, PubMed:1851162, PubMed:23481913). Works cooperatively with MutM and MutY to prevent accumulation in the DNA of oxidized guanine residues (PubMed:7739614)...

## Biological Role

Catalyzes 8-oxo-dGTP diphosphohydrolase (reaction.R09832), RXN-11396 (reaction.ecocyc.RXN-11396), RXN-11397 (reaction.ecocyc.RXN-11397), RXN-12816 (reaction.ecocyc.RXN-12816), RXN-14002 (reaction.ecocyc.RXN-14002). Bound by Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: Specifically hydrolyzes both 8-oxo-deoxyguanosine triphosphate (8-oxo-dGTP) and 8-oxo-guanosine triphosphate (8-oxo-GTP) to the related monophosphates, thereby cleaning up the nucleotide pools and preventing misincorporation of 8-oxoGua into DNA and RNA (PubMed:1309939, PubMed:15850400, PubMed:9311918). It prevents replicational errors by removing an oxidatively damaged form of guanine (8-oxo-dGTP) from DNA and the nucleotide pool (PubMed:1309939). 8-oxo-dGTP can be inserted opposite dA and dC residues of template DNA with almost equal efficiency thus leading to A.T to G.C transversions (PubMed:1309939). MutT may also ensure transcriptional fidelity, removing 8-oxo-GTP from the ribonucleotide triphosphate pool (PubMed:9311918). However, due to the lower efficiency of RNA polymerase 8-oxo-GTP incorporation, MutT is probably not a major contributor to transcriptional fidelity (PubMed:25294823). It also hydrolyzes 8-oxo-dGDP and 8-oxo-GDP to their monophosphate form (PubMed:15850400). In vitro, can also use dGTP, dGDP and other various nucleoside di- and triphosphates, with much lower efficiency (PubMed:1309939, PubMed:15850400, PubMed:1851162, PubMed:23481913). Works cooperatively with MutM and MutY to prevent accumulation in the DNA of oxidized guanine residues (PubMed:7739614). {ECO:0000269|PubMed:1309939, ECO:0000269|PubMed:15850400, ECO:0000269|PubMed:1851162, ECO:0000269|PubMed:23481913, ECO:0000269|PubMed:25294823, ECO:0000269|PubMed:7739614, ECO:0000269|PubMed:9311918}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R09832|reaction.R09832]] `KEGG` `database` - via EC:3.6.1.55
- `catalyzes` --> [[reaction.ecocyc.RXN-11396|reaction.ecocyc.RXN-11396]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-11397|reaction.ecocyc.RXN-11397]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-12816|reaction.ecocyc.RXN-12816]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14002|reaction.ecocyc.RXN-14002]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0099|gene.b0099]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08337`
- `KEGG:ecj:JW0097;eco:b0099;ecoc:C3026_00400;`
- `GeneID:944824;`
- `GO:GO:0000287; GO:0006203; GO:0006260; GO:0006281; GO:0006289; GO:0008413; GO:0030145; GO:0035539; GO:0044715; GO:0044716; GO:0046067`
- `EC:3.6.1.55`

## Notes

8-oxo-dGTP diphosphatase (8-oxo-dGTPase) (EC 3.6.1.55) (7,8-dihydro-8-oxoguanine-triphosphatase) (Mutator protein MutT) (dGTP pyrophosphohydrolase)
