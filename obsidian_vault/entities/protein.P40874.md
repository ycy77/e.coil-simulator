---
entity_id: "protein.P40874"
entity_type: "protein"
name: "solA"
source_database: "UniProt"
source_id: "P40874"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "solA b1059 JW1046"
---

# solA

`protein.P40874`

## Static

- Type: `protein`
- Source: `UniProt:P40874`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the oxidative demethylation of N-methyl-L-tryptophan. Can also use other N-methyl amino acids, including sarcosine, which, however, is a poor substrate. The solA gene product has N-methyltryptophan oxidase (MTOX) activity. Despite significant similarity to the Bacillus sp. sarcosine oxidase, the enzyme has comparatively little sarcosine oxidase activity . MTOX can catalyze the demethylation of various N-methyl amino acids, but has a preference for N-methyltryptophan . The metabolic role and physiological substrate for the enzyme are unknown. Cys308 is the covalent attachment site for FAD . Studies of the reaction mechanism are consistent with a modified ping pong mechanism and exclude the formation of a covalent adduct intermediate . Lys259 is the site of oxygen activation and also plays a role in holoenzyme biosynthesis and N-methyltryptophan oxidation. The enzyme contains separate active sites for N-methyltryptophan oxidation and oxygen reduction on opposite faces of the flavin ring . A crystal structure of SolA has been solved at 3.2 Å resolution, identifying Thr239 as a key residue for substrate side chain recognition . SolA expression is increased 3-fold by growth on minimal media . SolA: "sarcosine oxidase-like gene"

## Biological Role

Catalyzes RXN0-301 (reaction.ecocyc.RXN0-301). Bound by FAD (molecule.C00016).

## Annotation

FUNCTION: Catalyzes the oxidative demethylation of N-methyl-L-tryptophan. Can also use other N-methyl amino acids, including sarcosine, which, however, is a poor substrate.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-301|reaction.ecocyc.RXN0-301]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1059|gene.b1059]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P40874`
- `KEGG:ecj:JW1046;eco:b1059;ecoc:C3026_06440;`
- `GeneID:75203646;944983;`
- `GO:GO:0005829; GO:0006974; GO:0008115; GO:0050131; GO:0050660`
- `EC:1.5.3.-`

## Notes

N-methyl-L-tryptophan oxidase (MTOX) (EC 1.5.3.-)
