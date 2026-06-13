---
entity_id: "protein.P23874"
entity_type: "protein"
name: "hipA"
source_database: "UniProt"
source_id: "P23874"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hipA b1507 JW1500"
---

# hipA

`protein.P23874`

## Static

- Type: `protein`
- Source: `UniProt:P23874`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system, first identified by mutations that increase production of persister cells, a fraction of cells that are phenotypic variants not killed by antibiotics, which lead to multidrug tolerance (PubMed:16707675, PubMed:26222023, PubMed:6348026, PubMed:8021189). Persistence may be ultimately due to global remodeling of the persister cell's ribosomes (PubMed:25425348). Phosphorylates Glu-tRNA-ligase (AC P04805, gltX, on 'Ser-239') in vivo (PubMed:24095282, PubMed:24343429). Phosphorylation of GltX prevents it from being charged, leading to an increase in uncharged tRNA(Glu). This induces amino acid starvation and the stringent response via RelA/SpoT and increased (p)ppGpp levels, which inhibits replication, transcription, translation and cell wall synthesis, reducing growth and leading to persistence and multidrug resistance (PubMed:24095282, PubMed:24343429). Once the level of HipA exceeds a threshold cells become dormant, and the length of dormancy is determined by how much HipA levels exceed the threshold (PubMed:20616060). The hipA7 mutation (a double G22S D291A mutation) leads to increased generation of persister cells (cells that survive antibiotic treatment) probably by entering into a dormant state, as well as cold-sensitivity (PubMed:14622409, PubMed:16707675)...

## Biological Role

Catalyzes ATP:protein phosphotransferase; (reaction.R00162), RXN0-5211 (reaction.ecocyc.RXN0-5211). Component of HipAB toxin/antitoxin complex / DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-7425). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system, first identified by mutations that increase production of persister cells, a fraction of cells that are phenotypic variants not killed by antibiotics, which lead to multidrug tolerance (PubMed:16707675, PubMed:26222023, PubMed:6348026, PubMed:8021189). Persistence may be ultimately due to global remodeling of the persister cell's ribosomes (PubMed:25425348). Phosphorylates Glu-tRNA-ligase (AC P04805, gltX, on 'Ser-239') in vivo (PubMed:24095282, PubMed:24343429). Phosphorylation of GltX prevents it from being charged, leading to an increase in uncharged tRNA(Glu). This induces amino acid starvation and the stringent response via RelA/SpoT and increased (p)ppGpp levels, which inhibits replication, transcription, translation and cell wall synthesis, reducing growth and leading to persistence and multidrug resistance (PubMed:24095282, PubMed:24343429). Once the level of HipA exceeds a threshold cells become dormant, and the length of dormancy is determined by how much HipA levels exceed the threshold (PubMed:20616060). The hipA7 mutation (a double G22S D291A mutation) leads to increased generation of persister cells (cells that survive antibiotic treatment) probably by entering into a dormant state, as well as cold-sensitivity (PubMed:14622409, PubMed:16707675). Wild-type cells produce persisters at a frequency of 10(-6) to 10(-5) whereas hipA7 cells produce about 100-fold more persisters (PubMed:14622409, PubMed:16707675, PubMed:25425348). hipA7 decreases the affinity for antitoxin HipB, leading to increased HipA levels and persistence (PubMed:20616060); depending on the protein level, can be toxic enough to reduce cell growth or even kill cells. Generation of persister cells requires (p)ppGpp as cells lacking relA or relA/spoT generate fewer or no persister cells respectively compared to hipA7 (PubMed:14622409). The toxic effect of HipA is neutralized by its cognate antitoxin HipB (PubMed:20616060). Also neutralized by overexpression of gltX (PubMed:24343429, PubMed:28430938). With HipB acts as a corepressor for transcription of the hipBA promoter (PubMed:8021189); binding of HipA-HipB to DNA induces a 70 degree bend (PubMed:19150849, PubMed:26222023). This brings together and dimerizes 2 HipA molecules, which distorts the promoter region, preventing sigma-factor binding; additionally HipA and HipB would physically prevent RNA core polymerase from contacting the -35 promoter box (PubMed:26222023). May play a role in biofilm formation (PubMed:23329678). {ECO:0000269|PubMed:14622409, ECO:0000269|PubMed:16707675, ECO:0000269|PubMed:17041039, ECO:0000269|PubMed:19150849, ECO:0000269|PubMed:20616060, ECO:0000269|PubMed:23329678, ECO:0000269|PubMed:23667235, ECO:0000269|PubMed:24095282, ECO:0000269|PubMed:24343429, ECO:0000269|PubMed:25425348, ECO:0000269|PubMed:26222023, ECO:0000269|PubMed:28430938, ECO:0000269|PubMed:6348026, ECO:0000269|PubMed:8021189}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00162|reaction.R00162]] `KEGG` `database` - via EC:2.7.11.1
- `catalyzes` --> [[reaction.ecocyc.RXN0-5211|reaction.ecocyc.RXN0-5211]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-7425|complex.ecocyc.CPLX0-7425]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1507|gene.b1507]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23874`
- `KEGG:ecj:JW1500;eco:b1507;ecoc:C3026_08720;`
- `GeneID:946064;`
- `GO:GO:0000287; GO:0000976; GO:0001217; GO:0004674; GO:0005524; GO:0005829; GO:0006355; GO:0022611; GO:0032993; GO:0040008; GO:0043565; GO:0044010; GO:0046677; GO:0106310; GO:0110001`
- `EC:2.7.11.1`

## Notes

Serine/threonine-protein kinase toxin HipA (Ser/Thr-protein kinase HipA) (EC 2.7.11.1) (Toxin HipA)
